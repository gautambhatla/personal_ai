from llm_wrapper.localLLM.localLLM import LocalChatbot

llm = LocalChatbot()

def test_generate_response():
    prompt = "Hello, how are you?"
    response = llm.generate_response(prompt)
    print("Response:", response)

if __name__ == "__main__":
    test_generate_response()
    print("All tests passed.")