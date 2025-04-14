# Chatbot Application with Gemini API

This project implements a simple chatbot interface using Flask and the Gemini API. The chatbot can answer questions based on content fetched from a website. Follow these instructions to set up and run the application without errors.

## Prerequisites

Before you run the code, you need to install the necessary dependencies and set up the project.

---

## Step-by-Step Instructions

### 1. Download and Unzip the Project Folder

- Download the project zip file.
- Unzip the folder into a directory on your local machine.

The directory structure should look like this:

```
/project-directory
    /templates
        index.html
    api.env
    flask.py
```

---

### 2. Install Dependencies

You need to install the required Python libraries. Use the following command:

```bash
pip install flask requests python-dotenv beautifulsoup4
```

---

### 3. Get Your Gemini API Key

- Generate your API key from the Gemini API Key Generator.
- After you get the key, open the `api.env` file in a text editor.
- Replace the placeholder with your actual API key:

Example `api.env`:

```
GEMINI_API_KEY=your_actual_api_key
```

---

### 4. Ensure the File Structure

Make sure your project directory has the following files:

```
/project-directory
    /templates
        index.html
    api.env
    flask.py
```

---

### 5. Update the File Path for `.env`

In the `flask.py` file, ensure that the `load_dotenv()` function loads the correct path to the `api.env` file. Update the code like this:

```python
load_dotenv(r'full_path_to_your_api.env')
gemini_api_key = os.getenv("GEMINI_API_KEY")
```

Example:

```python
load_dotenv(r'D:\Project\Code\Chatbot\api.env')
```

---

### 6. Run the Flask Application

- Navigate to the project directory in your terminal.
- Run the Flask application:

```bash
python flask.py
```

- Open your browser and visit:
    
    `http://127.0.0.1:5000/`
    

---

### 7. Interacting with the Chatbot

Once the application is running, you can interact with the chatbot by typing a question in the input box.

The bot will fetch content from the website (for example, https://botpenguin.com/), process it, and return an answer based on that content.

---

## Troubleshooting

- **API Key Issue**:
    
    If you see an error saying "Gemini API Key not found," ensure that the API key in `api.env` is correctly set and the path is properly loaded.
    
- **Dependencies Issue**:
    
    If you encounter errors related to `requests`, `flask`, `beautifulsoup4`, or `python-dotenv`, make sure all dependencies are installed using:
    
    ```bash
    pip install flask requests python-dotenv beautifulsoup4
    ```
