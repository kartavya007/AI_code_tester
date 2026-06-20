from playwright_class import PersistentBrowser
from langchain_groq_class import Agent_class

Agent = Agent_class()
bot = PersistentBrowser(Agent , headless=False)
steps = [
    'navigate to the site https://www.saucedemo.com/' , 
    "enter the user name 'standard_user'" , 
    "enter the password 'secret_sauce'" ,
    "click login button" , 
    "Open Menu" , 
    "click logout"
    ]
bot.execute_step(steps=steps)
