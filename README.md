# 🐛 dataWorm-ai

**dataWorm-ai** is an intelligent AI Agent built with **Python**, **LangChain**, and **Google Gemini**.

It acts as a smart research assistant that can:
1.  **Search the Web** (using Tavily) for real-time information.
2.  **Scrape & Read** specific websites (using a custom Beautiful Soup tool) for deep analysis.
3.  **Remember** your conversation context (using SQLite memory) across different sessions.

---

## 🚀 Features

* **Brain:** Google Gemini 2.5 Flash (Fast & Large Context Window).
* **Memory:** Remembers user details and past queries using `langgraph` persistence.
* **Search:** Integrated with Tavily API for AI-optimized web search.
* **Scraping:** Custom-built tool to extract clean text from specific URLs, bypassing basic anti-bot headers.
* **Architecture:** Built on the modern **LangGraph** framework (ReAct Agent pattern).

---

## 🛠️ Prerequisites

* **Python 3.10+** (Tested on Python 3.13)
* **Google API Key** (for Gemini)
* **Tavily API Key** (for Web Search)

---

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Bhumi-2303/DataWorm-AI.git](https://github.com/Bhumi-2303/DataWorm-AI.git)
    cd DataWorm-AI
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv dataworm
    source dataworm/bin/activate  # On Windows: dataworm\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🔑 Configuration

1.  Create a file named `.env` in the root folder.
2.  Add your API keys inside it:

    ```ini
    # .env
    GOOGLE_API_KEY=AIzaSyD...<your_gemini_key>
    TAVILY_API_KEY=tvly-...<your_tavily_key>
    ```

    * *Get Gemini Key: [Google AI Studio](https://aistudio.google.com/)*
    * *Get Tavily Key: [tavily.com](https://tavily.com/)*

---

## 🏃 Usage

Run the agent from the terminal:

```bash
python main.py

Example Commands:

    Search: "What is the latest news on the release of Python 3.14?"

    Scrape: "Read this page https://example.com and summarize the main points."

    Complex: "Find the wikipedia page for 'Generative AI', read the History section, and tell me when it started."

    Memory: "My name is Bhumi." -> (Restart app) -> "Do you remember my name?"