from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# model = ChatGroq(model='llama-3.1-8b-instant')
model = ChatGroq(model='openai/gpt-oss-120b')

res = model.invoke('who owns twitter')

print(res.content)