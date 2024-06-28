import os
import replicate
import yaml
from flask import Flask, request, jsonify, render_template, Response
import os
from serpapi import GoogleSearch
import webbrowser
from threading import Timer
from werkzeug.serving import make_server

app = Flask(__name__)

# Load Replicate API key, change the Replicate API key in config.yaml file if the current one is not working
with open('config.yaml', 'r', encoding='UTF-8') as file:
    config = yaml.safe_load(file)
replicate_api_key = config['replicate']['api_key']
serpapi_api_key = config['serpapi']['api_key']
os.environ["REPLICATE_API_TOKEN"] = replicate_api_key
replicate_api_key = os.getenv('REPLICATE_API_TOKEN')
client = replicate.Client(api_token=replicate_api_key)

def perform_web_search(query):
    # Change the SerpApi api_key in config.yaml if the current one is not working
    params = {
        "q": query,
        "location": "California, United States",
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": serpapi_api_key,
        "num": "5"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if 'answer_box' in results:
        if 'result' in results['answer_box']:
            return(results['answer_box']['result'])
        elif 'snippet' in results['answer_box']:
            return(results['answer_box']['snippet'])
        elif 'definitions' in results['answer_box']:
            return(results['answer_box']['definitions'])
        else:
            organic_results=[]
            for i in range(len(results['organic_results'])):
                organic_results.append(results['organic_results'][i]['snippet'])
            return(organic_results)
    else:
        organic_results=[]
        for i in range(len(results['organic_results'])):
            organic_results.append(results['organic_results'][i]['snippet'])
        return(organic_results)

def process_llama_prompt(prompt):
    model = "meta/meta-llama-3-70b-instruct"
    output = []
    for event in replicate.stream(
        model,
        input={"prompt": prompt},
    ):
        output.append(str(event))
    return ''.join(output)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    searched_results = perform_web_search(question)
    prompt=f'The following results are the result from Google. Please utilize these provided results and your knowledge to answer the question: "{question}". Results from Google: {searched_results}.'
    response = process_llama_prompt(prompt)
    
    return jsonify({'response': response})

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return Response('<script>window.close()</script>', mimetype='text/html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        os._exit(0)
    func()

@app.route('/')
def index():
    return render_template('index.html')

def run_server():
    # Change the port here if 5000 is acquired by other applications
    server = make_server('127.0.0.1', 5000, app)
    server.serve_forever()

if __name__ == '__main__':
    # Change the port here if 5000 is acquired by other applications
    Timer(1, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    run_server()
