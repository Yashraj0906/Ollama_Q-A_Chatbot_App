# 💬 Enhanced Q&A Chatbot with Ollama

An intelligent **local chatbot** built using **Streamlit**, **LangChain**, and **Ollama**, capable of running open-source LLMs such as **Gemma**, **Phi-3**, and **Gemma-3:1B**.  
This app provides an easy-to-use interface for question answering with adjustable temperature and token settings — **no API key required**!

---

## ⚡ Features

✅ **Interactive Chat UI** — built with Streamlit  
✅ **Runs Fully Offline** using Ollama models  
✅ **Customizable Parameters** — temperature and max tokens  
✅ **LangChain-powered Prompt Management**  
✅ **Beautiful Sidebar Controls**  
✅ **Optional LangSmith Integration** for experiment tracking  

---

## ⚙️ Setup Instructions
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
