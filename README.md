# Agentic AI Web Automation Tester

A Python-based automation project that uses an AI model to interpret natural-language browser instructions and execute them with Playwright.

This project reads a list of test steps from `Steps.json`, sends each step to a Groq-powered agent, and then performs actions such as navigation, clicks, and form filling automatically.

---

## 🚀 Overview

The goal of this project is to let a user describe web actions in plain English and have the system convert those instructions into real browser actions.

Examples of supported actions include:
- Opening a website
- Clicking buttons
- Filling input fields
- Navigating to relevant pages
- Capturing screenshots after each step

---

## 📁 Project Structure

- `main.py`  
  Main entry point of the project. Loads environment variables, initializes the AI agent and browser automation class, and runs the steps.

- `playwright_class.py`  
  Handles browser setup, page navigation, screenshots, and execution of actions.

- `langchain_groq_class.py`  
  Connects to the Groq API and converts instructions into JSON actions that the browser can run.

- `Steps.json`  
  Stores the sequence of test instructions that the automation script will execute.

- `requirements.txt`  
  Lists all required Python packages.

- `Screenshots/`  
  Contains screenshot output captured during runs.

---

## 🛠️ Requirements

Make sure you have:
- Python 3.9+
- A valid Groq API key
- Playwright installed

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
Headless=true
```

### Variables
- `GROQ_API_KEY` → Your Groq API key
- `Headless` → Set to `true` for headless mode or `false` for visible browser mode

> Note: In the current code, `Headless` is read from the environment and passed to the browser setup. For best results, use the value exactly as `true` or `false`.

---

## ▶️ How to Run

Run the project using:

```bash
python main.py
```

The script will:
1. Load the environment settings
2. Read the steps from `Steps.json`
3. Ask the AI model to interpret each step
4. Execute the browser actions
5. Save screenshots for each step

---

## 🧪 Example Step Format

The `Steps.json` file contains steps like:

```json
{
  "step 1": "navigate to the site https://www.saucedemo.com/",
  "step 2": "enter the user name 'standard_user'",
  "step 3": "enter the password 'secret_sauce'",
  "step 4": "click login button"
}
```

The automation layer will try to map each step into a Playwright-compatible action.

---

## 📸 Screenshot Output

Each run generates a new folder inside `Screenshots/` with timestamped screenshots.

Example output:

```text
Screenshots/
  2026-06-21_16-41-05/
    step1.png
    step2.png
```

---

## ⚠️ Notes

- The AI response must be valid JSON for the automation script to work correctly.
- The success of locator detection depends on the page DOM and the instruction quality.
- This project is useful for testing and experimenting with AI-assisted browser automation.

---

## 💡 Future Improvements

Possible improvements for the project:
- Better error handling for invalid AI responses
- More reliable locator generation
- Support for additional action types
- Logging and reporting
- GUI or web dashboard for configuring automation steps

---

## License

This project is intended for learning, experimentation, and automation testing purposes.
