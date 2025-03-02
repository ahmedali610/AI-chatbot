AI Chatbot Application (FastAPI + Streamlit + Falcon-7B)
A simple chatbot web application powered by the Falcon-7B model from Hugging Face. This project uses FastAPI for the backend and Streamlit for the frontend, providing an interactive way for users to communicate with the AI.

Visit the GitHub Repository

Features
FastAPI Backend: Handles chat message requests, processes them, and interfaces with the Falcon-7B model via Hugging Face API.
Streamlit Frontend: Provides a user-friendly interface for users to interact with the chatbot.
Docker Compose: Uses Docker Compose to simplify running both backend and frontend as Docker containers.
Project Structure
bash
Copy
Edit
AI-chatbot/
│-- backend/                # FastAPI Backend
│   │-- main.py             # FastAPI application code
│   │-- .env                # Environment variables (e.g., API keys)
│   │-- requirements.txt    # Backend dependencies
│   │-- Dockerfile          # Backend Docker setup
│-- frontend/               # Streamlit Frontend
│   │-- app.py              # Streamlit frontend application
│   │-- requirements.txt    # Frontend dependencies
│   │-- Dockerfile          # Frontend Docker setup
│-- docker-compose.yml      # Docker Compose configuration
│-- README.md               # Project documentation
│-- .gitignore              # Git ignore file
Installation
Prerequisites
Docker: Ensure Docker and Docker Compose are installed. You can download Docker from here.
Python: If you are not using Docker, you need Python 3.10 or higher installed.
1. Clone the repository
Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/ahmedali610/AI-chatbot.git
cd AI-chatbot
Running the Backend (FastAPI)
1. Set Up the Backend
Navigate to the backend directory:

bash
Copy
Edit
cd backend
Create a .env file in the backend directory to store your Hugging Face API key:

bash
Copy
Edit
HUGGINGFACE_API_KEY=your_huggingface_api_key
Install Backend Dependencies:

Install the required Python dependencies for the backend:

bash
Copy
Edit
pip install -r requirements.txt
Run the Backend:

Start the FastAPI server:

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000
The backend will be accessible at http://localhost:8000.

Running the Frontend (Streamlit)
1. Set Up the Frontend
Navigate to the frontend directory:

bash
Copy
Edit
cd frontend
Install Frontend Dependencies:

Install the required Python dependencies for the frontend:

bash
Copy
Edit
pip install -r requirements.txt
Run the Frontend:

Start the Streamlit app:

bash
Copy
Edit
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
The frontend will be accessible at http://localhost:8501.

Running Both Services Using Docker Compose
To run both backend and frontend services together using Docker Compose:

1. Build and Start Both Services
From the root directory of the project (where the docker-compose.yml file is located), run the following command:

bash
Copy
Edit
docker-compose up --build
This will build and start the backend and frontend containers.

2. Access the Services
Frontend (Streamlit): Open http://localhost:8501 in your browser to interact with the chatbot UI.
Backend (FastAPI): The API will be available at http://localhost:8000 to handle chat requests.
3. Stop the Services
To stop the services, run:

bash
Copy
Edit
docker-compose down
This will stop and remove all containers.

API Endpoints
POST /chat/
Description: Sends a message to the chatbot and receives a response.

Request Body:

json
Copy
Edit
{
  "user_id": "string",
  "message": "string"
}
user_id: Unique identifier for the user (to maintain chat history).
message: The user's message to the chatbot.
Response:

json
Copy
Edit
{
  "response": "string",
  "history": [
    {
      "role": "USER",
      "message": "string"
    },
    {
      "role": "ASSISTANT",
      "message": "string"
    }
  ]
}
response: The chatbot's response to the user's message.
history: The conversation history, including both user and assistant messages.
GET /
Description: Returns a simple message indicating that the API is running.
Response:
json
Copy
Edit
{
  "message": "Chatbot API is running!"
}
Technology Stack
Backend: FastAPI
Frontend: Streamlit
Model: Falcon-7B (via Hugging Face API)
Containerization: Docker
API: Hugging Face Inference API
Python: 3.10
Contributing
Contributions are welcome! Feel free to fork this project, open issues, and submit pull requests.

Fork the repository
Create a new branch
Make your changes
Open a pull request with a detailed description of your changes
