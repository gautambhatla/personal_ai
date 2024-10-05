import os

GEMINI_MODEL = os.environ.get('GEMINI_MODEL', "gemini-1.5-flash") 
api_key = os.environ.get('API_KEY', '')

MAX_TOKENS = 1000
TEMPERATURE = 0.7
SYSTEM_PROMPT = "You are a helpful chatbot, your response must be concise and to the point."