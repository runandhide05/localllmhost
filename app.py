from flask import Flask, render_template, request, Response, jsonify
import requests
import json

app = Flask(__name__)

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'response': 'Error: No message provided.'}), 400
        
        user_message = data['message']  # Get the message from the JSON payload
    else:
        # For GET requests
        user_message = request.args.get('message')
        if not user_message:
            return jsonify({'response': 'Error: No message provided.'}), 400

    # Define the headers for the POST request
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "max_tokens": 1024,
        "stream": True  # Enabling streaming
    }

    # Send the POST request to the LM Studio API
    response = requests.post(LM_STUDIO_URL, headers=headers, json=payload, stream=True)
    
    if response.status_code == 200:
        def generate_stream():
            buffer = ""

            for chunk in response.iter_lines():
                if chunk:
                    chunk_decoded = chunk.decode('utf-8').strip()

                    if chunk_decoded.startswith("data: "):
                        json_chunk = chunk_decoded[6:] 

                        if json_chunk == "[DONE]":
                            break

                        try:
                            response_data = json.loads(json_chunk)
                            token_content = response_data['choices'][0]['delta'].get('content', '')

                            if token_content:
                                token_content = token_content.replace('\n', '<br>')
                                buffer += token_content  # Accumulate the content
                                yield f"data: {token_content}\n\n"  # Yield each token as it is received
                        except json.JSONDecodeError:
                            print("Error decoding JSON from chunk:", json_chunk)


        return Response(generate_stream(), content_type='text/event-stream')
    else:
        return jsonify({'response': 'Error: Could not reach the model.'}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
