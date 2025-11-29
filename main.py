import os
from dotenv import load_dotenv
from agent import build_agent
from langchain_core.messages import HumanMessage

load_dotenv()

def main():
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return

    print("🐛 dataWorm-ai (Memory + Search Edition) is ready!")
    agent = build_agent()

    # This config tells the bot which conversation "thread" to remember.
    # If you want a fresh chat, change "thread_id" to a new number (e.g., "2")
    config = {"configurable": {"thread_id": "1"}}

    print("Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Bye! I'll remember this for next time.")
            break
            
        try:
            print("🐛 Thinking...")
            
            # Pass the 'config' so it knows to use memory
            response = agent.invoke(
                {"messages": [HumanMessage(content=user_input)]},
                config=config
            )
            
            # Clean up response (remove signature if present)
            raw_content = response["messages"][-1].content
            if isinstance(raw_content, list):
                ai_answer = "".join([item['text'] for item in raw_content if 'text' in item])
            else:
                ai_answer = raw_content
            
            print(f"\nAI: {ai_answer}\n")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()