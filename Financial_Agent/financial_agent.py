# Created by trilo at 28-12-2024
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
load_dotenv()


os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["PHI_API_KEY"] = os.getenv("PHI_API_KEY")

# web search agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the wen for the imformation",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instruction=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# financial agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True)
    ],
    instructions=["Use table to display data"],
    show_tools_cols=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include source", "Use table to shpw data"],
    show_tools_cols=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA",
                              stream=True)
