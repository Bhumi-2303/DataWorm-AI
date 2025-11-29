import os
import sqlite3  # <--- Needed for manual connection
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_community.tools.tavily_search import TavilySearchResults
from tools.scraper_tool import WebScrapeTool

# --- FIX START ---
# Instead of .from_conn_string, we connect manually so it doesn't close on us.
# check_same_thread=False is important for Agent apps.
conn = sqlite3.connect("worm_memory.db", check_same_thread=False)
memory = SqliteSaver(conn)
# --- FIX END ---

def build_agent():
    # 1. Initialize Gemini
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0
    )

    # 2. Define Tools
    search_tool = TavilySearchResults(
        max_results=3,
        description="Use this to search for websites, news, or general information."
    )

    scrape_tool = WebScrapeTool()
    scrape_tool.description = "Use this ONLY when the user gives you a specific URL to read, or when you need to read the full content of a page found by search."
    
    tools = [search_tool, scrape_tool]

    # 3. Create the Agent
    return create_react_agent(model=llm, tools=tools, checkpointer=memory)