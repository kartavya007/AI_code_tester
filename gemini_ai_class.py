from groq import Groq
import json
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

class Agent_class:
    def __init__(self , key , model):
        # key = os.getenv('GROQ_API_KEY')
        # model = os.getenv('AI_Model')
        self.output_schema = {
            "type": "OBJECT",
            "properties": {
                "action": {
                    "type": "STRING", 
                    "enum": ["goto", "click", "fill"],
                    "description": "The specific type of Playwright action to perform."
                },
                "locator": {
                    "type": "STRING", 
                    "description": "The URL target or the computed Playwright locator selector string."
                },
                "text": {
                    "type": "STRING", 
                    "description": "The text to input. Generate ONLY if the action type is 'fill', otherwise set to null or omit."
                }
            },
            # Ensure the model always yields action and locator
            "required": ["action", "locator"]
        }
        self.client = genai.Client(api_key=key)
        self.model = model
    def html_dom_parser(self , description , dom = None):
        user_content = f"""
        Description of the step - {description}
        DOM - {dom}
        """
        completion = self.client.models.generate_content(
            model=self.model,
            contents=user_content,
            config=types.GenerateContentConfig(
                # Pass system rules directly into the config parameter
                system_instruction="""
                    You are a very helpful QA tester. You help in parsing the browser DOM and identifying the most suitable locator that should be used by the tester in order to perform the testing. 
                    
                    Inputs to rely on:
                    1. The HTML content of the page
                    2. Description of the locator 
                    
                    *Note: The HTML step can be skipped if a direct locator or URL is present in the description string.
                    
                    The locator provided must be fully compatible with a Playwright testing script (e.g., page.goto(<url>), page.locator(<locator>)). 
                    Try to prioritize using ID selectors over any other attributes when parsing the DOM elements.
                """,
                response_mime_type="application/json",
                response_schema=self.output_schema
            )
        )
        print(completion.text)
        return json.loads(completion.text)

if __name__ == '__main__':
    agent = Agent_class()
    f = open('dom.html' , 'r')
    text = f.read()
    f.close()
    ans = agent.html_dom_parser("Navigate to the site https://www.saucedemo.com/")
    print(ans)
