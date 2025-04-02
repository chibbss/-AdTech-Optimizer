import os

os.environ["CREWAI_DISABLE_ANALYTICS"] = "true"
from crewai import Crew
from textwrap import dedent
from agents import AdTechAgents
from tasks import AdTechTasks
from langchain.tools import DuckDuckGoSearchRun

# Initialize search tool (if needed)
search_tool = DuckDuckGoSearchRun()

# Set up API keys from environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "default_api_key")
os.environ["OPENAI_ORGANIZATION"] = os.getenv("OPENAI_ORGANIZATION_ID", "default_org_id")


class CustomCrew:
    def __init__(self, campaign_data):
        self.campaign_data = campaign_data


    def run(self):
        # Initialize agent and task classes
        agents = AdTechAgents()
        tasks = AdTechTasks()

        # Define agents
        tier_manager = agents.tier_management_agent(self.campaign_data)
        conversion_agent = agents.conversion_prediction_agent(self.campaign_data)
        budget_agent = agents.budget_allocation_agent(self.campaign_data)
        bid_optimization_agent = agents.bid_optimization_agent(self.campaign_data)
        ad_personalization_agent = agents.ad_personalization_agent(self.campaign_data)

        # Define tasks
        tier_manager_task = tasks.tier_management_task(tier_manager, self.campaign_data)
        conversion_task = tasks.conversion_prediction_task(conversion_agent, self.campaign_data)
        budget_task = tasks.budget_allocation_task(budget_agent, self.campaign_data)
        bid_task = tasks.bid_optimization_task(bid_optimization_agent, self.campaign_data)
        ad_personalization_task = tasks.ad_personalization_task(ad_personalization_agent, self.campaign_data)

        # Set up the AI crew
        crew = Crew(
            agents=[tier_manager, conversion_agent, budget_agent, bid_optimization_agent, ad_personalization_agent],
            tasks=[tier_manager_task, conversion_task, budget_task, bid_task, ad_personalization_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to AdBirt AI Ad Campaign Analysis")
    print("--------------------------------------------")

    campaign_data = input(dedent("""Enter campaign details (JSON format recommended): """))

    custom_crew = CustomCrew(campaign_data)
    result = custom_crew.run()

    print("\n\n########################")
    print("## Custom AdBirt AI Run Result:")
    print("########################\n")
    print(result)