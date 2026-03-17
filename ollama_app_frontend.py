import streamlit as st
from ollama_app_backend import chatboot

# 1. Page Config & Custom CSS
# Setting up the Streamlit page configuration with title, icon, and layout
st.set_page_config(page_title="AI Research Assistant", page_icon="🤖", layout="centered")

# Custom CSS for a cleaner look
# Applying custom styles to change background color and button appearance
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Displaying the main title and caption for the app
st.title("🤖 Ollama Research Assistant")
st.caption("Powered by Local Ollama LLM")

# 2. Sidebar for Controls
# Creating a sidebar for user controls and settings
with st.sidebar:
    st.header("Settings")
    # Button to clear the conversation history
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    # Displaying information about the system status
    st.info("System: Ollama LLM is ready. Experience fast, private AI chat locally!")

# 3. Conversation History Initialization
# Initializing the session state to store conversation messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display Chat History (Chat Bubbles Style)
# Looping through the stored messages and displaying them in chat message containers
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input (Bottom Fixed Input)
# Checking if the user has entered input via the chat input widget
if user_input := st.chat_input("Ask me anything about your documents..."):
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Save to session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # 6. Get AI Response with Loading Spinner
    # Displaying the assistant's response in a chat message container with a spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking and searching..."):
            try:
                # Backend invoke
                # Calling the backend function to get the AI response
                result = chatboot.invoke({"question": user_input})
                # Check agar backend "answer" return kar raha hai ya "generation"
                # Extracting the answer from the result, checking for 'answer' or 'generation' keys
                answer = result.get("answer") or result.get("generation") or "No response generated."
                
                # Displaying the answer in the chat
                st.markdown(answer)
                
                # Save to session state
                # Adding the assistant's response to the conversation history
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                # Handling any errors that occur during the backend call
                st.error(f"Error: {e}")
