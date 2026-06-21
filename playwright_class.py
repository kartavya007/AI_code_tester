from playwright.sync_api import sync_playwright
from time import sleep
from langchain_groq_class import Agent_class
import datetime
import os
from pathlib import Path
class PersistentBrowser:
    def __init__(self, Agent : Agent_class , folder : str = 'Screenshots' , Steps : list = None , headless: bool = True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.headless = headless
        self.content = None
        self.steps = Steps
        self.agent = Agent
        time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.path = f"{folder}\\{time}"
        Path(self.path).mkdir(parents=True , exist_ok=True)
    
    def navigate(self , action):
        ans = self.agent.html_dom_parser(action , self.content)
        if ans['action'] == 'goto':
            self.page.goto( ans['locator'])
        if  ans['action'] == 'click':
            self.page.locator( ans['locator']).click()
        if  ans['action'] == 'fill':
            self.page.locator( ans['locator']).fill( ans['text'])
        self.content = self.page.content()
        sleep(10)
        
    def execute_step(self , steps :list = None):
        if self.steps == None:
            if steps == None:
                raise Exception('Steps can not be empty')
            self.steps = steps
        i = 1
        for step in steps:
            self.navigate(step)
            screen_shot_name = f"{self.path}\\step{i}.png"
            self.page.screenshot(path=screen_shot_name)
            i += 1
        
    def close(self):
        self.browser.close()
        self.playwright.stop()
# --- Example Usage ---
if __name__ == "__main__":
    # 1. Initialize and launch
    bot = PersistentBrowser(headless=False)
    # page = bot.launch()
    bot.navigate('goto' , 'https://www.saucedemo.com/')
    bot.navigate('fill' , "input[id='user-name']" , 'standard_user')
    bot.close()
    
    # 2. Do your automation tasks here
    
    # page.goto("https://example.com")
    # print(f"Page title is: {page.title()}")

    # # 3. Hand control over to the user
    # bot.keep_alive()