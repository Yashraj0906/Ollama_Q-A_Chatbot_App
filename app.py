import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith tracking (optional, for logging)
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot with Ollama"

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries clearly and helpfully."),
        ("user", "Question: {question}")
    ]
)

# Define function to generate a response
def generate_response(question, engine, temperature, max_tokens):
    llm = Ollama(model=engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# Streamlit UI
st.title("💬 Enhanced Q&A Chatbot with Ollama")

# Sidebar options
engine = st.sidebar.selectbox("Select Ollama model", ["gemma2", "phi3", "gemma3:1b"])
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

# User input
st.write("🧠 Ask me anything below:")
user_input = st.text_input("You:")

if user_input:
    with st.spinner("Generating response... please wait ⏳"):
        response = generate_response(user_input, engine, temperature, max_tokens)
    st.subheader("Assistant:")
    st.write(response)
else:
    st.info("Please type a question above to start chatting.")
