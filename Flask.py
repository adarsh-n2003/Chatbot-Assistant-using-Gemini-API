from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os
from bs4 import BeautifulSoup

# Load API Key from .env file
load_dotenv(r'D:\Document\Code\Projects\Chatbot\Final Project\api.env')
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Verify API Key
if not gemini_api_key:
    raise ValueError("Gemini API Key not found. Please check your .env file.")

app = Flask(__name__)

# Function to fetch website content
def fetch_website_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract all text content from the webpage, focusing on headings and paragraphs
        paragraphs = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        text_content = "\n".join([p.get_text(strip=True) for p in paragraphs])
        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

# Function to process and structure website data into headings and paragraphs
def process_website_data(raw_data):
    # We can split data based on headings (h1, h2, etc.)
    sections = {}
    lines = raw_data.splitlines()
    current_section = None
    
    for line in lines:
        line = line.strip()
        if line.startswith(("Key Features", "Target Audience", "Product Details", "FAQ")):
            current_section = line
            sections[current_section] = []
        elif current_section and line:
            sections[current_section].append(line)
        elif line:
            if "General Information" not in sections:
                sections["General Information"] = []
            sections["General Information"].append(line)
                
    return sections

# Function to query the Gemini API with the structured request
def query_gemini_api(user_input, website_data, model="gemini-v1"):
    """
    Queries the Gemini API with user input and website data.

    Args:
        user_input (str): The user's query.
        website_data (dict): The processed and structured website content.
        model (str): The model to use (default: gemini-v1).

    Returns:
        str: The chatbot's response or an error message.
    """
    # Build a prompt for Gemini API based on structured sections
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_api_key}"
    headers = {"Content-Type": "application/json"}
    
    # Assuming the website content is broken into structured categories
    structured_prompt = f"Answer the following query based on the structured website content.\n\n"
    
    structured_prompt += f"Website Data:\n"
    for category, items in website_data.items():
        structured_prompt += f"\n**{category}:**\n"
        for item in items:
            structured_prompt += f"- {item}\n"
    
    structured_prompt += f"\nQuery: {user_input}\n"

    payload = {"contents": [{"parts": [{"text": structured_prompt}]}]}

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if 'candidates' in data:
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            return "Error: Invalid response from Gemini API."
    except requests.exceptions.RequestException as e:
        return f"Error with the Gemini API: {e}"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        website_url = "https://botpenguin.com/"  # Example website URL
        website_content = fetch_website_content(website_url)
        if website_content:
            structured_data = process_website_data(website_content)
            chatbot_response = query_gemini_api(user_input, structured_data)
            return render_template("index.html", response=chatbot_response, user_input=user_input)
    return render_template("index.html", response=None)

if __name__ == "__main__":
    app.run(debug=True)
