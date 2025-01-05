# Created by trilo at 29-12-2024
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app
import os
import phi

load_dotenv()

phi.api = os.getenv("PHI_API_KEY")

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

app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
