Local LLM WebUI

An interactive chat platform built using a custom AI model hosted via LM Studio, designed for real-time AI responses with streaming capabilities. The platform provides users with engaging conversations powered by loaded model.


Features

•	Real-time AI Conversations: Users can chat with an AI and receive streaming responses.

•	Streaming Responses: The application streams AI responses token-by-token to give users a smooth, uninterrupted experience.

•	Interactive Frontend: A user-friendly web interface for messaging with the AI.

Tech Stack

•	Backend: Flask (Python) for handling API requests and responses.

•	Frontend: HTML, CSS, JavaScript for the chat interface.

•	Streaming: Server-Sent Events (SSE) for real-time message streaming.

Setup
Requirements

1.	Python 3.7+
2.	Flask and requests Python packages
3.	LM Studio running locally.
   
•   Configure LM Studio

Ensure LM Studio is running with the appropriate model.
Running the Application
1.	Start the Flask Server
python app.py
2.	Access the Frontend
Open your browser and navigate to http://localhost:5001.

Usage

Once the application is running, you can:
1.	Type a message into the chat input box.
2.	Press Enter or click the Send button.
3.	The AI will stream its response in real time below your message.
   
Known Issues

•	Response Stream Cuts Off: Occasionally, the stream may stop prematurely due to client disconnection or timeout. Future versions will handle reconnection or stream resumption.

•	Frontend Formatting: Responses containing newlines might not render properly. Current workaround: converting \n to <br> in the frontend.

License


This project is licensed under the MIT License. See the LICENSE file for more details.
