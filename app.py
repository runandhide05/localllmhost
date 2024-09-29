from flask import Flask, render_template, request, Response, jsonify
import requests
import json

app = Flask(__name__)

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"

conversation_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    global conversation_history 

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'response': 'Error: No message provided.'}), 400
        
        user_message = data['message']
    else:
        user_message = request.args.get('message')
        if not user_message:
            return jsonify({'response': 'Error: No message provided.'}), 400

    conversation_history.append({"role": "user", "content": user_message})

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "messages": conversation_history,  # Send the entire conversation history
        "model": "lmstudio-community/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
        "max_tokens": 1024,
        "stream": True  # Enabling streaming
    }

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
                                buffer += token_content 
                                yield f"data: {token_content}\n\n"
                        except json.JSONDecodeError:
                            print("Error decoding JSON from chunk:", json_chunk)

            conversation_history.append({"role": "assistant", "content": buffer})

        return Response(generate_stream(), content_type='text/event-stream')
    else:
        return jsonify({'response': 'Error: Could not reach the model.'}), 500

@app.route('/clear', methods=['POST'])
def clear_history():
    global conversation_history
    conversation_history = []  # Reset the conversation history
    return jsonify({'response': 'Conversation history cleared.'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
