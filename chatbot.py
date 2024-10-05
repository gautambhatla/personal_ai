import streamlit as st
from llm_wrapper.gemini import gemini

genai = gemini.GeminiChatbot()

def main_page():
    _, center, _ = st.columns([4,10,4])
    with center.container():
        chat_container()



def update_chat(chat_placeholder, chat_history):
    chat_placeholder.empty()
    with chat_placeholder.container():
            st.markdown(
                """
                <style>
                .chat-message-u{
                    background-color: #f0f0f0; /* Grey background */
                    border-radius: 10px; /* Rounded corners */
                    padding: 10px; /* Some padding */
                    margin: 10px 0; /* Spacing above and below */
                    max-width: 60%; /* Limit the width */
                    text-align: left; /* Align text to left inside the bubble */
                    float: right; /* Align the bubble to the right */
                }

                .chat-message-a{
                    background-color: #f0f0f0; /* Grey background */
                    border-radius: 10px; /* Rounded corners */
                    padding: 10px; /* Some padding */
                    margin: 10px 0; /* Spacing above and below */
                    max-width: 60%; /* Limit the width */
                    text-align: left; /* Align text to left inside the bubble */
                    float: left; /* Align the bubble to the right */
                }

                </style>
                """,
                unsafe_allow_html=True
            )
            # Display chat history
            for message in chat_history:
                if message['role'] == 'user':
                    st.markdown(f"<div class='chat-message-u user'>{message['content']}</div>", unsafe_allow_html=True)
                else:
                    # st.markdown(f"<div class='chat-message-a assistant'>{message['content']}</div>", unsafe_allow_html=True)
                    st.markdown(message['content'])
                    
def chat_container():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Reverse the chat history for displaying messages in the correct order
    chat_history = st.session_state.chat_history

    with st.container():
        chat_placeholder = st.empty()
        update_chat(chat_placeholder, chat_history)
        
    styl = f"""
    <style>
        .stChatInput {{
        position: fixed;
        bottom: 3rem;
        }}
    </style>
    """
    st.markdown(styl, unsafe_allow_html=True)
    user_prompt = st.chat_input('Ask Chatbot...')

    
    if user_prompt:
        st.session_state.chat_history.append({'role': 'user', 'content': user_prompt})
        with chat_placeholder.container():
            update_chat(chat_placeholder, chat_history)
        response = genai.generate_response(user_prompt)

        assistant_response = response
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

        # Update chat container with new messages
        chat_history = st.session_state.chat_history
        update_chat(chat_placeholder, chat_history)