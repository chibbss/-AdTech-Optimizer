from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging
from main import CustomCrew  # Ensure this imports your CrewAI implementation
import json

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
    target_country: str
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
        analysis = ai_crew.run()  # Run AI analysis

        # ✅ DEBUG: Check AI response format
        print(f"DEBUG: AI Crew Output - {analysis}")

        # ✅ Ensure response is a dictionary
        if isinstance(analysis, str):
            try:
                analysis = json.loads(analysis)
            except json.JSONDecodeError:
                raise HTTPException(status_code=500, detail=f"Invalid response format from AI crew: {analysis}")
        elif not isinstance(analysis, dict):
            raise HTTPException(status_code=500, detail=f"Unexpected AI crew response type: {type(analysis)}")

        # **Extract only the selected agent's output**
        response_data = {"status": "success"}

        if campaign_request.agent_selected == "conversion_prediction":
            response_data["conversion_prediction"] = analysis.get("conversion_prediction", "No data available")
        elif campaign_request.agent_selected == "budget_allocation":
            response_data["budget_suggestion"] = analysis.get("budget_suggestion", "No data available")
        elif campaign_request.agent_selected == "bid_optimization":
            response_data["bid_strategy"] = analysis.get("bid_strategy", "No data available")
        elif campaign_request.agent_selected == "ad_personalization":
            response_data["personalization_notes"] = analysis.get("personalization_notes", "No data available")
        else:
            response_data["message"] = "Invalid agent selection"

        return response_data

    except Exception as e:
        logger.error(f"Error analyzing campaign: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# **RUN FASTAPI APP**
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)