import streamlit as st
import ollama
import time

# Set up page configuration
st.set_page_config(page_title="Interactive Chatbot", page_icon="🤖", layout="wide")
st.title("BuddyBot 🛠️")
# Gradient background styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
        }
        .chat-container {
            max-width: 75%; /* Adjusts the width of the chat bubble */
            padding: 15px;
            margin-top: 10px;
            border-radius: 15px;
            word-wrap: break-word;
            display: inline-block;
        }
        
        .greeting {
            font-size: 1.4rem;
            font-weight: bold;
            color: #5D3FD3;
            animation: fadeIn 2s ease-in;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for name and model selection
with st.sidebar:
    st.header("Settings")
    user_name = st.text_input("How can I call you?", placeholder="Enter your name")
    model_choice = st.selectbox("Choose a model for the chatbot:", ["llama3.2", "llama3.1", "llama2","nemotron-mini","codegeex4","mistral"])
    st.session_state.model = model_choice


# Display a greeting with animation
if user_name:
    st.markdown(f"<div class='greeting'>Hello, {user_name}! 👋</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='greeting'>Hello! 👋</div>", unsafe_allow_html=True)
st.text(" ")
# Title and session state for messages

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?", "avatar": "🤖"}]

# Display Message History with enhanced avatars and improved text alignment
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user", avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message("assistant", avatar=msg.get("avatar", "🤖")).write(msg["content"])
    # st.markdown(
    #     f"""
    #     <div class="chat-container {message_class}">
    #         <span class="{avatar_class}"></span><span>{msg['content']}</span>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

# Generate response with streaming
def generate_response():
    response = ollama.chat(model=st.session_state.model, stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield st.session_state["full_message"]

# Chat input with response streaming
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)

    # Initialize response and animated message streaming
    st.session_state["full_message"] = ""
    response_container = st.chat_message("assistant", avatar="🤖")
    
    # Initialize response text area for streaming
    response_text = response_container.empty()

    for message in generate_response():
        response_text.markdown(message)
        time.sleep(0.05)  # Animation delay for streaming effect

    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
