from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

from starlette.responses import JSONResponse

from main import CustomCrew
import json
from typing import Union, List # to set multiple target countries

# Initialize FastAPI app
app = FastAPI(title="AdBirt AI Campaign Analysis API", version="1.0")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define campaign request model
class CampaignRequest(BaseModel):
    user_tier: str
    agent_selected: str
    campaign_name: str
    campaign_objective: str
    campaign_description: str
    campaign_destination: str
    banner_size: str
    banner_type: str
    daily_ad_budget: float
    start_date: str
    end_date: str
    target_country: Union[str, List[str]]  # Can be either a string or a list of strings
    media_url: str


# **ROOT LANDING PAGE**
@app.get("/")
async def root():
    return {
        "message": "Welcome to AdBirt AI API",
        "endpoints": {
            "health_check": "/health",
            "campaign_analysis": "/campaign/analyze (POST)"
        }
    }


# **HEALTH CHECK ENDPOINT**
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running"}


# **405 HANDLING FOR GET ON /campaign/analyze/**
@app.get("/campaign/analyze/")
async def method_not_allowed():
    return {"status": "error", "message": "Method Not Allowed. Use POST instead."}


# **CAMPAIGN ANALYSIS ENDPOINT**
@app.post("/campaign/analyze/")
async def analyze_campaign(campaign_request: CampaignRequest):
    """Handles campaign data, verifies user tier, and delegates to AI agents."""

    campaign_data = campaign_request.dict()
    logger.info(f"Received campaign data: {campaign_data}")

    try:
        ai_crew = CustomCrew(campaign_data)
        final_result = ai_crew.run()

        # If it's a custom class (like CrewOutput), force it into a dict
        if hasattr(final_result, "dict"):
            final_result = final_result.dict()
        elif hasattr(final_result, "__dict__"):
            final_result = final_result.__dict__

        # If it's a string, try parsing it
        if isinstance(final_result, str):
            try:
                final_result = json.loads(final_result)
            except json.JSONDecodeError:
                raise HTTPException(status_code=500,
                                    detail=f"Invalid JSON string returned from AI crew: {final_result}")

        return JSONResponse(content={"status": "success", "data": final_result}, status_code=200)

    except Exception as e:
        logger.error(f"Error analyzing campaign: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# **RUN FASTAPI APP**
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)