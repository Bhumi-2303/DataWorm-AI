import requests
from bs4 import BeautifulSoup
from typing import Type
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool

class ScrapeInput(BaseModel):
    url: str = Field(description="The full URL of the website to scrape")

class WebScrapeTool(BaseTool):
    name: str = "web_scraper"
    description: str = "Useful for extracting text content from specific website URLs."
    args_schema: Type[BaseModel] = ScrapeInput

    def _run(self, url: str) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for script in soup(["script", "style", "nav", "footer"]):
                script.decompose()

            return soup.get_text(separator=' ', strip=True)[:8000]

        except Exception as e:
            return f"Error scraping {url}: {str(e)}"