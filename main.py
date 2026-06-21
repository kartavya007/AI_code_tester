from playwright_class import PersistentBrowser
from langchain_groq_class import Agent_class
from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv('GROQ_API_KEY')
ai_model = 'openai/gpt-oss-120b'
Agent = Agent_class(key=key , model=ai_model)
bot = PersistentBrowser(Agent , headless=True)
steps = [
    'navigate to the site https://www.saucedemo.com/' , 
    "enter the user name 'standard_user'" , 
    "enter the password 'secret_sauce'" ,
    "click login button" , 
    "Open Menu" , 
    "click logout"
    ]
bot.execute_step(steps=steps)
