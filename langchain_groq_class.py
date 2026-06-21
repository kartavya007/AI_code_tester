from groq import Groq
import json
from dotenv import load_dotenv
import os

class Agent_class:
    def __init__(self , key , model):
        # key = os.getenv('GROQ_API_KEY')
        # model = os.getenv('AI_Model')
        self.client = Groq(
                    api_key=key
                )
        self.model = model
    def html_dom_parser(self , description , dom = None):
        completion = self.client.chat.completions.create(
            model=self.model , 
            messages=[{"role":"system" , 
                       "content": """
                            You are a very helpfull QA tester you help in parsing the browser DOM and indentify the most suitable locator that can should be used by the tester in order to perform the testing. 
                            ---------------------------------------------------------------------------
                            For providing the output you need some input except that you won't provide the locator 
                            1. The HTML content of the page
                            2. Description of the locator 
                            
                            **Note - 1st step can be skipped if any locator is present in the description or direct URL is there 
                            ---------------------------------------------------------------------------
                            The locator provided to the tester should be compatible to playwright testing script and that can be directly used in the playwright script
                            example - page.goto(<url>) , page.locator(<locator>) ...etc
                            try to use ID where ever possible rather than anyother variable
                            --------------------------------------------------------------------------
                            output provided should be in the json format sample format is provided below
                            {
                                "action": "goto|click|fill" (any one) , 
                                "locator": "<url>|<locator>" (any one) , 
                                "text" : "<text to be filled>" (output should be provided only if the action type in fill else return null)
                            }
                            
                            *Note - JSON should be in legal format
                            1. For string use double qoutes ("")
                            2. null for None
                            3. it should parse with python module json.loads()
                       """} , 
                      {
                          'role' : 'user' , 
                          'content' : f"""
                          Description of the step - {description} , 
                          DOM - {dom}
                          """
                          
                      }
                      ]
        )
        print(completion.choices[0].message.content)
        return json.loads(completion.choices[0].message.content)

if __name__ == '__main__':
    agent = Agent_class()
    f = open('dom.html' , 'r')
    text = f.read()
    f.close()
    ans = agent.html_dom_parser("Navigate to the site https://www.saucedemo.com/")
    print(ans)
