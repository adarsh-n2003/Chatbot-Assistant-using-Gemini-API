Chatbot Application with Gemini API
 This project implements a simple chatbot interface using Flask and the Gemini API. The chatbot can answer questions 
based on content fetched from a website. Follow these instructions to set up and run the application without errors.
 Prerequisites
 Before you run the code, you need to install the necessary dependencies and set up the project.
 Step-by-Step Instructions
 Download and Unzip the Project Folder
 Download the project zip file.
 Unzip the folder into a directory on your local machine.
 The directory structure should look like this:
 /project-directory
 /templates
 index.html
 api.env
 flask.py
  Install Dependencies
 You need to install the required Python libraries. Use the following command to install them:
 pip install flask requests python-dotenv beautifulsoup4
 Get Your Gemini API Key
 You need to replace the placeholder API key with your actual Gemini API key.
 To get your API key, visit 
Gemini API Key Generator and generate your key.
 After you get the key, open the 
api.env file in a text editor and replace the placeholder 
api.env:
 GEMINI_API_KEY=your_actual_api_key
  Ensure the File Structure
 Make sure your project directory has the following files and folder structure:
 /project-directory
 /templates
 index.html
 api.env
 flask.py
 Update the File Path for 
In the 
.env
 flask.py file, ensure that the 
code to:
 flask.py:
 API_KEY with your actual key:
 load_dotenv() function is loading the correct path for the 
.env file. Update the 
load_dotenv(r'api.env_file_location')  # Example: load_dotenv(r'D:\Project\Code\Chatbot
 \api.env')
 gemini_api_key = os.getenv("GEMINI_API_KEY")
 Readme
 1
Replace 
'api.env_file_location' with the actual path where the 
api.env file is located on your machine. For example:
 load_dotenv(r'D:\Project\Code\Chatbot\api.env')
  Run the Flask Application
 Navigate to the project directory in your terminal.
 Run the Flask application with the following command:
 python flask.py
 This will start the Flask server, and you can visit the chatbot interface in your browser at 
 Interacting with the Chatbot
 http://127.0.0.1:5000/ .
 Once the application is running, you can interact with the chatbot by typing a question in the input box.
 The bot will fetch the content from the given website (in this case, 
https://botpenguin.com/ ), process the content, and 
return an answer based on the content.
 Troubleshooting
 API Key Issue If you see an error saying "Gemini API Key not found," ensure that the API key in 
set.
 api.env is correctly 
Dependencies Issue If any dependencies are missing or you encounter errors related to 
requests , 
flask , 
beautifulsoup4 , or 
python-dotenv , make sure all dependencies are installed as mentioned in Step 2.
