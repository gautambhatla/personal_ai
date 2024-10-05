import google.generativeai as genai
from .config import (
    api_key,
    GEMINI_MODEL,
    MAX_TOKENS,
    TEMPERATURE,
    SYSTEM_PROMPT,
)

class GeminiChatbot:
    def __init__(self, model_name=GEMINI_MODEL):
        self.model=genai.GenerativeModel(
            model_name=model_name,
            system_instruction=SYSTEM_PROMPT)
        genai.configure(api_key=api_key)
        self.chat_history = []


    def generate_response(self, prompt, max_output_tokens=MAX_TOKENS, temperature=TEMPERATURE):
        """Generate a text response based on a prompt."""
        response = self.model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_output_tokens,
                temperature=temperature,
            )
        )
        return response.text


if __name__ == "__main__":
    chatbot = GeminiChatbot()
    
