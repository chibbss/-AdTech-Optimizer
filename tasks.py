from crewai import Task
from textwrap import dedent

class AdTechTasks:
    def conversion_prediction_task(self, agent, campaign_data):
        """Task for predicting ad campaign conversion probability."""
        return Task(
            description=dedent(f"""
                1. Analyze the given ad campaign details, including {campaign_data} 
                   (campaign name, description, budget, duration, target audience, etc.).
                2. Compare the campaign details with industry benchmarks and similar past campaigns.
                3. Utilize AI-driven insights to estimate the probability (%) of the campaign converting.
                4. Provide a detailed breakdown of factors influencing the conversion rate, 
                   including strengths, weaknesses, and potential optimizations.
            """),
            expected_output=dedent(f"""
                A structured conversion analysis report containing:
                - Predicted % conversion probability.
                - Key factors influencing conversion.
                - Suggested optimizations for better results.
            """),
            agent=agent,
        )

    def budget_allocation_task(self, agent, campaign_data):
        """Task for optimizing ad spend allocation."""
        return Task(
            description=dedent(f"""
                1. Analyze the budget distribution in {campaign_data}.
                2. Determine whether the current budget allocation is optimal.
                3. Recommend changes to maximize campaign effectiveness.
                4. Provide insights on cost-efficient allocation strategies.
            """),
            expected_output=dedent(f"""
                A budget allocation strategy including:
                - Current inefficiencies in the budget.
                - Recommendations for optimized spend.
                - Expected improvement in ROI.
            """),
            agent=agent,
        )

    def bid_optimization_task(self, agent, campaign_data):
        """Task for optimizing ad bid strategies."""
        return Task(
            description=dedent(f"""
                1. Analyze real-time bid request data from OpenRTB auctions.
                2. Evaluate bid floor prices, competition intensity, and historical win rates.
                3. Determine the optimal bid amount to maximize win probability while minimizing cost.
                4. Provide a dynamic bid strategy for real-time ad placement.
            """),
            expected_output=dedent(f"""
                A bid optimization report including:
                - Suggested bid amount for the auction.
                - Probability of winning based on historical trends.
                - Cost-efficiency analysis for the proposed bid.
            """),
            agent=agent,
        )

    def ad_personalization_task(self, agent, campaign_data):
        """Task for personalizing ad creatives based on audience targeting."""
        return Task(
            description=dedent(f"""
                1. Analyze audience demographics and engagement in {campaign_data}.
                2. Identify potential ad personalization improvements.
                3. Generate customized ad recommendations for different audience segments.
                4. Provide creative insights for better engagement.
            """),
            expected_output=dedent(f"""
                A detailed ad personalization report including:
                - Recommended creative variations.
                - Expected engagement improvements.
                - AI-driven insights for content tailoring.
            """),
            agent=agent,
        )

    def tier_management_task(self, agent, campaign_data):
        """Task for verifying user access level and delegating to the correct AI agent."""
        return Task(
            description=dedent(f"""
                1. Analyze {campaign_data} to verify the user’s subscription tier.
                2. Determine which AI-powered features they can access (Conversion, Budgeting, Bidding, Personalization).
                3. Apply any necessary restrictions based on their plan.
                4. Pass the {campaign_data} to the appropriate AI agent for execution.
                
            """),
            expected_output=dedent(f"""
                - The campaign data is validated, and access is granted.
                - The data is successfully passed to the selected AI agent for execution.
            """),
            agent=agent,
        )