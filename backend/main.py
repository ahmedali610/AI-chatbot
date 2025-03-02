import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set API Key and Model Name
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = "tiiuae/falcon-7b-instruct"

# Initialize Hugging Face Inference Client
client = InferenceClient(model=MODEL_NAME, token=HUGGINGFACE_API_KEY)

app = FastAPI()

# Store chat history
chat_histories: Dict[str, List[Dict[str, str]]] = {}
MAX_HISTORY = 5  # Reduce history to avoid excessive repetition

# Define request model
class ChatRequest(BaseModel):
    user_id: str  
    message: str

@app.post("/chat/")
def chat(request: ChatRequest):
    """Handles user queries and maintains chat history."""
    try:
        # Get/initialize user history
        history = chat_histories.get(request.user_id, [])

        # Define system prompt (sets chatbot personality)
        system_prompt = (
            "You are an AI assistant designed to be friendly, helpful, and professional. "
            "Keep responses concise, clear, and engaging. Avoid unnecessary repetition. "
            "Respond naturally while maintaining politeness and accuracy.\n"
        )

        # Format chat history with clear separation
        formatted_history = ""
        for h in history:
            formatted_history += f"{h['role']}: {h['message']}\n"

        # Prepare the prompt
        prompt = f"{system_prompt}{formatted_history}USER: {request.message}\nASSISTANT:"

        # Get model response using text generation with temperature
        chatbot_response = client.text_generation(prompt, max_new_tokens=150, temperature=0.8)

        # Clean response to remove unwanted prefixes and trim unnecessary repetition
        chatbot_response = chatbot_response.replace("USER:", "").replace("USER", "").replace("ASSISTANT:", "").replace("User", "").strip()

        # Ensure the response is different from the last one
        if history and chatbot_response == history[-1]["message"]:
            chatbot_response = "Let me think... Here's something different: " + chatbot_response

        # Update chat history with only the latest interactions
        history.append({"role": "USER", "message": request.message})
        history.append({"role": "ASSISTANT", "message": chatbot_response})
        chat_histories[request.user_id] = history[-MAX_HISTORY:]  # Keep only the last 5 exchanges

        return {"response": chatbot_response, "history": history}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root(): 
    return {"message": "Chatbot API is running!"} 

