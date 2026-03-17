# Ollama Research Assistant

This project is a simple and interactive Streamlit web interface that connects to a locally installed large language model (LLM) running via Ollama.

## Features
- Text input box for user queries
- Response area to display model-generated answers
- Conversation history panel
- Reset button to clear conversation
- Smooth communication between Streamlit frontend and Ollama LLM backend

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start your local Ollama LLM (ensure the model is running).
3. Launch the Streamlit app:
   ```bash
   streamlit run frontend.py
   ```

## Project Structure
- `frontend.py`: Streamlit web interface
- `backend.py`: Backend logic connecting to Ollama LLM
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation

## Notes
- Make sure Ollama is installed and running locally.
- The app is designed for fast, private AI chat on your machine.

## License
MIT
