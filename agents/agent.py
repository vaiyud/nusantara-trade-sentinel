# imports
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools import AgentTool

from tools.query_tool import get_bq_tool
from tools.search_tool import get_search_tool

# setup credentials & configuration
load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
DATA_ID = os.getenv("DATASET_ID")

bq_tool = get_bq_tool()
search_tool = get_search_tool()

# pdf analyst agent
analyst_agent = Agent(
    name="analyst_specialist",
    model=os.getenv("AGENT_MODEL"),
    description="Specialist in reading BNM and MIDA annual reports and economic reviews.",
    instruction="""You are a senior economic analyst. Your job is to extract qualitative 
    insights from official reports. 
    
    MANDATORY CITATION RULE: 
    Every factual statement or explanation MUST be followed by a citation in parentheses. 
    Example: 'The E&E sector saw a decline due to the global tech downcycle (from BNM Annual Report 2023).'
    
    If you are unsure of the source, state (from Internal Policy Library).""",
    tools=[search_tool]
)

# data analyst agent
quantitative_agent = Agent(
    name="quant_specialist",
    model=os.getenv("AGENT_MODEL"),
    description="Specialist in analyzing structured economic data like GDP, CPI, and Trade volumes.",
    instruction=f"""You are a data scientist. Use BigQuery to answer questions about numbers. 
    You have access to tables: cpi_data, gdp_data, and trade_data.
    Your GCP Project ID is: {PROJECT_ID}
    Your Dataset ID is: {DATA_ID}
    
    You MUST only use data from the following tables:
    - projectId: "{PROJECT_ID}", datasetId: "{DATA_ID}", tableId: "cpi_data"
    - projectId: "{PROJECT_ID}", datasetId: "{DATA_ID}", tableId: "gdp_data"
    - projectId: "{PROJECT_ID}", datasetId: "{DATA_ID}", tableId: "trade_data"

    MANDATORY CITATION RULE:
    Every numerical finding must cite the database table it came from.
    Example: 'GDP growth for 2023 was 3.7% (from gdp_data table).

    Always write valid SQL and summarize the numerical trends clearly.""",
    tools=[bq_tool]
)

# commander agent - orchestrator
root_agent = Agent(
    name="trade_sentinel_command",
    model=os.getenv("AGENT_MODEL"),
    description="The main entry point for the Nusantara Trade Sentinel.",
    instruction="""You are the Nusantara Trade Sentinel.
    - If you need numbers or SQL, use the quantitative_agent.
    - If you need policy context or report details, use the analyst_agent.
    - If there is an image, analyze it yourself using your vision.
    Combine all insights into a single professional response.""",
    tools=[AgentTool(agent=analyst_agent), AgentTool(agent=quantitative_agent)]
)

root_agent = root_agent