# Chatbot Application with Gemini API

This project implements a simple chatbot interface using Flask and the Gemini API. The chatbot can answer questions based on content fetched from a website. Follow these instructions to set up and run the application without errors.

---

## Prerequisites

Before you run the code, you need to install the necessary dependencies and set up the project.

---

## Step-by-Step Instructions

### 1. Download and Unzip the Project Folder

- Download the project zip file.
- Unzip the folder into a directory on your local machine.

The directory structure should look like this:

```
bash
CopyEdit
/project-directory
    /templates
        index.html
    api.env
    flask.py

```

---

### 2. Install Dependencies

Install the required Python libraries by running:

```bash
bash
CopyEdit
pip install flask requests python-dotenv beautifulsoup4

```

---

### 3. Get Your Gemini API Key

- Generate your API key from the Gemini API Key Generator (Google AI Studio).
- Open the `api.env` file.
- Replace the placeholder with your actual API key:

Example `api.env`:

```
ini
CopyEdit
GEMINI_API_KEY=your_actual_api_key

```

---

### 4. Ensure the File Structure

Make sure your project directory has the following structure:

```
bash
CopyEdit
/project-directory
    /templates
        index.html
    api.env
    flask.py

```

---

### 5. Update the File Path for `.env`

In the `flask.py` file, ensure that the `load_dotenv()` function loads the correct path to the `api.env` file. Update it like this:

```python
python
CopyEdit
load_dotenv(r'full_path_to_your_api.env')
gemini_api_key = os.getenv("GEMINI_API_KEY")

```

Example:

```python
python
CopyEdit
load_dotenv(r'D:\Project\Code\Chatbot\api.env')

```

---

### 6. Changing the Website URL

By default, the chatbot fetches content from:

```python
python
CopyEdit
https://botpenguin.com/

```

If you want the chatbot to answer based on a **different website**, simply update the `website_url` inside `flask.py`:

```python
python
CopyEdit
website_url = "https://your-new-website.com/"

```

> Note: Make sure the new website has accessible text content (like paragraphs and headings) so the bot can extract useful data.
> 

---

### 7. Run the Flask Application

- Navigate to the project directory in your terminal.
- Run the Flask application:

```bash
bash
CopyEdit
python flask.py

```

- Open your browser and visit:

```
cpp
CopyEdit
http://127.0.0.1:5000/

```

---

### 8. Interacting with the Chatbot

Once the application is running, type your questions into the input box.

The chatbot will fetch website content, process it intelligently, and generate an answer based on the retrieved data.

---

## Troubleshooting

- **API Key Issue**:
    - If you see an error like "Gemini API Key not found," ensure that the API key in `api.env` is correctly set and the path is correct.
- **Dependencies Issue**:
    - If you encounter module errors (`requests`, `flask`, `beautifulsoup4`, `python-dotenv`), install them again:
    
    ```bash
    bash
    CopyEdit
    pip install flask requests python-dotenv beautifulsoup4
    
    ```
    
- **Website Content Fetch Error**:
    - If the bot cannot fetch content from the given URL, make sure the website allows scraping and has readable text.
