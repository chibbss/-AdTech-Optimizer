# AdBirt AI Campaign Analysis API

A FastAPI-based backend service that leverages CrewAI and various AI agents to analyze and optimize advertising campaigns.

## Overview

This API provides AI-powered insights for digital advertising campaigns, offering various analysis features based on user subscription tier:

- **Conversion Prediction**: Analyzes campaign metrics to predict conversion probabilities
- **Budget Allocation**: Optimizes ad spend distribution for maximum ROI
- **Bid Optimization**: Determines optimal bid prices for real-time bidding (RTB) auctions
- **Ad Personalization**: Tailors ad creatives based on audience targeting

## Subscription Tiers

There is a dedicated tier management agent that works with the  different feature sets based on the user's subscription plan:

- **Basic Plan ($5/month)**: Conversion Prediction, Budget Allocation
- **Pro Plan ($9/month)**: Ad Personalization, Conversion Prediction, Budget Allocation, Priority Support
- **Advanced Plan ($10.99/month)**: Conversion Prediction, Bid Optimization, Budget Allocation
- **Enterprise Plan ($12.99/month)**: Ad Personalization, Conversion Prediction, AI-Driven Recommendation, Account Management, Budget Allocation

## API Endpoints

### Health Check
```
GET /health
```
Returns the status of the API.

### Campaign Analysis
```
POST /campaign/analyze/
```
Analyzes campaign data based on the selected agent and user tier.

#### Request Format
```json
{
  "user_tier": "Basic",
  "agent_selected": "conversion_prediction",
  "campaign_name": "Trendluxe Spring Collection",
  "campaign_objective": "Boost sales for new fashion line",
  "campaign_description": "Launching a new luxury fashion collection targeting high-end customers.",
  "campaign_destination": "https://trendluxe.com/spring-collection",
  "banner_size": "300x250",
  "banner_type": "Static",
  "daily_ad_budget": 50.00,
  "start_date": "2025-04-01",
  "end_date": "2025-04-30",
  "target_country": "United States",
  "media_url": "https://trendluxe.com/banner.jpg"
}
```

#### Response Format
Depending on the agent selected, the response will contain different fields:

**Conversion Prediction**:
```json
{
  "status": "success",
  "conversion_prediction": {
    "probability": 67.5,
    "factors": [...],
    "recommendations": [...]
  }
}
```

**Budget Allocation**:
```json
{
  "status": "success",
  "budget_suggestion": {
    "current_inefficiencies": [...],
    "optimized_allocation": [...],
    "expected_roi_improvement": "15%"
  }
}
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- OpenAI API key
- DuckDuckGo search tool (optional)

### Environment Variables
Create a `.env` file in the project root with the following variables:
```
OPENAI_API_KEY=your_openai_api_key
OPENAI_ORGANIZATION_ID=your_organization_id
```

### Installation
1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   uvicorn api:app --reload
   ```

## Example Usage

### cURL

```bash
curl -X POST "http://localhost:8000/campaign/analyze/" \
     -H "Content-Type: application/json" \
     -d '{
          "user_tier": "Basic",
          "agent_selected": "conversion_prediction",
          "campaign_name": "Trendluxe Spring Collection",
          "campaign_objective": "Boost sales for new fashion line",
          "campaign_description": "Launching a new luxury fashion collection targeting high-end customers.",
          "campaign_destination": "https://trendluxe.com/spring-collection",
          "banner_size": "300x250",
          "banner_type": "Static",
          "daily_ad_budget": 50.00,
          "start_date": "2025-04-01",
          "end_date": "2025-04-30",
          "target_country": "United States",
          "media_url": "https://trendluxe.com/banner.jpg"
        }'
```

### Python

```python
import requests
import json

url = "http://localhost:8000/campaign/analyze/"
headers = {"Content-Type": "application/json"}
payload = {
    "user_tier": "Basic",
    "agent_selected": "conversion_prediction",
    "campaign_name": "Trendluxe Spring Collection",
    "campaign_objective": "Boost sales for new fashion line",
    "campaign_description": "Launching a new luxury fashion collection targeting high-end customers.",
    "campaign_destination": "https://trendluxe.com/spring-collection",
    "banner_size": "300x250",
    "banner_type": "Static",
    "daily_ad_budget": 50.00,
    "start_date": "2025-04-01",
    "end_date": "2025-04-30",
    "target_country": "United States",
    "media_url": "https://trendluxe.com/banner.jpg"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
```

## Architecture

The system is built on these core components:
- **FastAPI**: Handles HTTP requests and responses
- **CrewAI**: Orchestrates the AI agents working together
- **OpenAI Models**: Powers the AI capabilities (GPT-3.5-Turbo, GPT-4o-Mini, GPT-4o)

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful operation
- 405: Method not allowed
- 500: Internal server error with details

## Logging

The system uses Python's built-in logging module configured at the INFO level.

## License

MIT