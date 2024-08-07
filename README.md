# AI-Agent-for-Web-Search-Using-LLaMA-3

# AI Agent Web Search

This project is a web-based AI agent that performs web searches using LLaMA 3 model and SerpApi API. It uses Flask as the web framework and Replicate as the platform to run the LLaMA 3 model.

## Features

- Perform web searches using GoogleSearch API through SerpApi API
- Generate responses using LLaMA 3 model through Replicate API
- Web interface for interacting with the AI agent

## Requirements

- Python==3.11.4
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
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using pip.

```bash
pip install -r requirements.txt
```

### 4. Set API Token
Change your Replicate and SerpApi API token in config.yaml file if needed.<br>

```bash
replicate:
  api_key: your_replicate_api_key
serpapi:
  api_key: your_serpapi_api_key
```

### 5. Set the sever port
The sever port is default to 5000.<br>
Change the sever port if other application is taking that port.<br>
```bash
def run_server():
    # Change the port here if 5000 is acquired by other applications
    server = make_server('127.0.0.1', your_port_number, app)
    server.serve_forever()

if __name__ == '__main__':
    # Change the port here if 5000 is acquired by other applications
    Timer(1, lambda: webbrowser.open('http://127.0.0.1:your_port_number/')).start()
    run_server()
```

### 6. Run the Flask Server
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
This project is licensed under the GNU General Public License v3.0 License.

## Contact
If you have any questions or feedback, feel free to reach out to alexliu0121@gmail.com.
