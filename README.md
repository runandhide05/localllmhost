AI Chat Platform
An interactive chat platform built using a custom AI model hosted via LM Studio, designed for real-time AI responses with streaming capabilities. The platform provides users with engaging conversations powered by the loaded model.

Table of Contents
Features
Tech Stack
Setup
Requirements
Installation
Running the Application
Usage
Known Issues
License
Features
Real-time AI Conversations: Users can chat with an AI and receive streaming responses.
Streaming Responses: The application streams AI responses token-by-token, providing a smooth and uninterrupted experience.
Interactive Frontend: A user-friendly web interface for messaging with the AI.
Tech Stack
Backend: Flask (Python) for handling API requests and responses.
Frontend: HTML, CSS, and JavaScript for the chat interface.
Streaming: Server-Sent Events (SSE) for real-time message streaming.
Setup
Requirements
Python 3.7+
Flask and requests Python packages
LM Studio running locally with a loaded model
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/runandhide05/localllmhost.git
cd ai-chat-platform
Set up a Python Virtual Environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Running the Application
Ensure LM Studio is Running

Ensure that LM Studio is running with the appropriate model loaded.

Start the Flask Server

bash
Copy code
python app.py
Access the Frontend

Open your browser and navigate to http://localhost:5001.

Usage
Once the application is running, follow these steps:

Type a message into the chat input box.
Press Enter or click the Send button.
The AI will stream its response in real time below your message.
Known Issues
Response Stream Cuts Off: Occasionally, the stream may stop prematurely due to client disconnection or timeout. Future versions will handle reconnection or stream resumption.
Frontend Formatting: Responses containing newlines may not render properly. The current workaround is to convert \n to <br> in the frontend.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
