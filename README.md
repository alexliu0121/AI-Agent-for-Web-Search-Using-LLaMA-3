# AI-Agent-for-Web-Search-Using-LLaMA-3

# AI Agent Web Search

This project is a web-based AI agent that performs web searches using OpenAI's LLaMA 3 model and DuckDuckGo API. It uses Flask as the web framework and Replicate as the platform to run the LLaMA 3 model.

## Features

- Perform web searches using GoogleSearch API through SerPapi API
- Generate responses using LLaMA 3 model through Replicate API
- Web interface for interacting with the AI agent

## Notes

- Noted that the api keys I'm using is free so it's not unlimited
- Both Replicate and SerPapi have very limited amount of free usage
- If there's any authentication errors, that means it reaches the limitation
- Feel free to contact me if you need another API key to evaluate the function of the agent

## Requirements

- Python 3.11.4
- Flask==3.0.3
- google_search_results==2.4.2
- PyYAML==6.0.1
- PyYAML==6.0.1
- replicate==0.26.1
- serpapi==0.1.5
- Werkzeug==3.0.3

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/alexliu0121/AI-Agent-for-Web-Search-Using-LLaMA-3.git
cd AI-Agent-for-Web-Search-Using-LLaMA-3
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required packages using pip.

```bash
pip install -r requirements.txt
```

### 4. Set Replicate API Token
Change your Replicate API token in config.yaml file if needed.<br>

```bash
replicate:
  api_key: your_replicate_api_key
serpapi:
  api_key: your_serpapi_api_key
```

### 5. Run the Flask Server
Start the Flask server. The server will automatically open your default web browser to the web interface.

```bash
python app.py
```

## Usage
Enter your question in the input field and click "Ask" to get a response from the AI agent.<br>
Click "Clear" to clear the response area.<br>
Click "Shutdown" to shut down the server and close the browser window.<br>

## File Structure
```plaintext
.
├── app.py                  # Main Flask application
├── config.yaml             # Configuration file for the project
├── requirements.txt        # List of project dependencies
└── templates
    └── index.html          # HTML template for the web interface
```

Example Commands
Start the server:
```bash
python app.py
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## License
This project is licensed under the MIT License.

## Contact
If you have any questions or feedback, feel free to reach out to alexliu0121@gmail.com.
