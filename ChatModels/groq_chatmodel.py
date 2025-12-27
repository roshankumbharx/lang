from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant')

res = model.invoke('who won the nobel prize in 2025 in physics')

print(res.content)