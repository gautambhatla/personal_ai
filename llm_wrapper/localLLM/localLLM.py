import requests
from llm_wrapper.localLLM.config import (
    MODEL,
    MAX_TOKENS,
    TEMPERATURE,
    LLM_URL
)

class LocalChatbot:
    def __init__(self, model_name=MODEL):
        self.url = LLM_URL
        self.model_name = model_name
        self.chat_history = []


    def generate_response(self, prompt, max_output_tokens=MAX_TOKENS, temperature=TEMPERATURE):
        """Generate a text response based on a prompt."""
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "max_tokens": max_output_tokens,
            "temperature": temperature
        }

        response = requests.post(self.url, json=payload)
        if response.ok:
            data = response.json()
            return data.get("response", "No response generated.")
        else:
            print("Request failed:", response.status_code, response.text)
    
if __name__ == "__main__":
    # Example usage
    chatbot = LocalChatbot()
    prompt = "Hello, how are you?"
    response = chatbot.generate_response(prompt)
    print("Chatbot response:", response)
