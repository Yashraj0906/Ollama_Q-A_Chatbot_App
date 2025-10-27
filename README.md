🧠 Enhanced Q&A Chatbot with Ollama

This is a Streamlit web app powered by LangChain and Ollama that allows users to interact with locally hosted open-source LLMs like Gemma, Phi-3, and Gemma-3:1B.
It provides a simple question-and-answer interface with adjustable parameters such as temperature and token limit.

🚀 Features

💬 Interactive chatbot using LangChain’s prompt pipeline

⚙️ Choose Ollama models dynamically (e.g., gemma2, phi3, gemma3:1b)

🔥 Adjustable temperature and max token sliders

🧩 Uses LangChain for structured prompts and output parsing

⚡ Runs locally using Ollama — no external API key required

🧠 Optional integration with LangSmith for model tracing and debugging

🗂️ Project Structure
📁 GenAI Projects/
│
├── app.py                # Main Streamlit app
├── .env                  # Environment variables (optional)
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone (https://github.com/Yashraj0906/Ollama_Q-A_Chatbot_App.git)
cd Ollama_Chatbot_App

2️⃣ Create a virtual environment
python -m venv .venv


Activate it:

Windows: .\.venv\Scripts\activate

macOS/Linux: source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install and run Ollama

Download Ollama: https://ollama.com/download

Then pull your desired model:

ollama pull gemma2
# or
ollama pull phi3
# or
ollama pull gemma3:1b


Verify installation:

ollama list

5️⃣ Run the app
streamlit run app.py
