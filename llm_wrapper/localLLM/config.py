import os

MODEL = os.environ.get('MODEL', "llama3.2") 
LLM_URL = "http://localhost:11434/api/generate"
MAX_TOKENS = 1000
TEMPERATURE = 0.7
SYSTEM_PROMPT = "You are a helpful chatbot, your response must be concise and to the point."