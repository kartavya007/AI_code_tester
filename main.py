from playwright_class import PersistentBrowser
from langchain_groq_class import Agent_class
from dotenv import load_dotenv
import os
import json

if __name__ == '__main__':
    load_dotenv()
    key = os.getenv('GROQ_API_KEY')
    ai_model = 'openai/gpt-oss-120b'
    headless = os.getenv('Headless')
    Agent = Agent_class(key=key , model=ai_model)
    bot = PersistentBrowser(Agent , headless=bool(headless))
    f = open('Steps.json')
    dic_steps = json.loads(f.read())
    steps = []
    for i in dic_steps:
        steps.append(dic_steps[i])
    bot.execute_step(steps=steps)
