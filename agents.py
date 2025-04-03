from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


class AdTechAgents:
    def __init__(self):
        """Initialize AI models based on access tiers."""
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4omini = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
        self.OpenAIGPT4o = ChatOpenAI(model_name="gpt-4o", temperature=0.7)

    def conversion_prediction_agent(self, campaign_data):
        """Agent to predict conversion probability of ad campaigns."""
        return Agent(
            role="Facebook and Google Ads Conversion Prediction Specialist",
            goal="Analyze advertising campaign metrics and predict the (%) probability of conversion with data-driven accuracy.",
            backstory=dedent(f"""
                You are an expert digital advertising analyst at AdBirt Performance, 
                a top ad optimization firm. Your role is to assess ad campaigns based on the user's {campaign_data}, 
                industry benchmarks, and marketing insights. Using advanced AI and statistical analysis, 
                you estimate the likelihood of a campaign successfully converting.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4omini,
            multimodal_input=True,
        )

    def budget_allocation_agent(self, campaign_data):
        """Agent for optimizing ad spend allocation."""
        return Agent(
            role="Facebook and Google Ads Budget Allocation Specialist",
            goal="Optimize the budget allocation of an ad campaign to maximize reach and ROI.",
            backstory=dedent(f"""
                You are an expert in financial allocation for digital advertising at AdBirt Finance. 
                Your job is to analyze the user's {campaign_data}, determine the most effective budget split, 
                and suggest improvements for better performance.
            """),
            verbose=True,
            llm=self.OpenAIGPT4omini,
            multimodal_input=True,
        )

    def bid_optimization_agent(self, campaign_data):
        """Agent for real-time OpenRTB bid optimization."""
        return Agent(
            role="Real-Time OpenRTB Bid Optimization Specialist",
            goal="Determine the optimal bid price for ad auctions to maximize win rate while maintaining cost efficiency.",
            backstory=dedent(f"""
                You are an advanced AI-powered bidding strategist specializing in OpenRTB auctions at AdBirt AI. 
                Your expertise lies in dynamically analyzing {campaign_data} and real-time bid requests from ad exchanges 
                to predict the best bid price for each auction.

                You consider:
                - **Campaign Goals:** Advertiser's budget, max bid limits, and strategy.
                - **Auction Dynamics:** Floor price, ad slot details, and competing bids.
                - **Historical Performance:** Past win rates and bid efficiency.
                - **User Data:** Device type, location, browsing behavior, and relevance.

                Your job is to analyze these factors and **predict the best bid amount** that balances **winning probability & cost-effectiveness** 
                while ensuring the advertiser stays within budget.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4omini,
            multimodal_input=True,
        )

    def ad_personalization_agent(self, campaign_data):
        """Agent for personalizing ad creatives based on audience targeting."""
        return Agent(
            role="AI-Driven Ad Personalization Specialist",
            goal="Analyze and tailor ad creatives for different audience segments to boost engagement.",
            backstory=dedent(f"""
                You are a specialist in AI-powered ad personalization at AdBirt Creative. 
                Your role is to analyze {campaign_data}, recommend personalized ad variations, 
                and optimize creative assets for maximum audience resonance.
            """),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4o,
            multimodal_input=True,
        )

    def tier_management_agent(self, campaign_data):
        """Agent that determines user access level based on subscription plan."""
        return Agent(
            role="Subscription Tier(Plan) Manager",
            goal="Verify user plan access and delegate the campaign data to the correct AI agent.",
            backstory=dedent(f"""
                You are the Subscription Tier(Plan) Manager at AdBirt AI. Your job is to verify the user's access level
                and ensure they can only use the AI tools available in their subscription plan.

                **Official Subscription Plans & Features:**
                - **Basic Plan ($5/month):**  
                  - Conversion Prediction  
                  - Budget Allocation  

                - **Pro Plan ($9/month):**  
                  - Ad Personalization  
                  - Conversion Prediction  
                  - Budget Allocation  
                  - Priority Support  

                - **Advanced Plan ($10.99/month):**  
                  - Conversion Prediction  
                  - Bid Optimization  
                  - Budget Allocation  

                - **Enterprise Plan ($12.99/month):**  
                  - Ad Personalization  
                  - Conversion Prediction  
                  - AI-Driven Recommendation  
                  - Account Management  
                  - Budget Allocation  

                Your task is to analyze the {campaign_data}, determine the user’s tier, and route the campaign 
                to the appropriate AI-powered agent. Ensure they are only granted access to features included 
                in their current subscription plan.
            """),
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT35,
        )