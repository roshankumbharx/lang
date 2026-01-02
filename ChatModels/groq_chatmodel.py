from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant')
# model = ChatGroq(model='openai/gpt-oss-120b')
# model = ChatGroq(model='groq/compound')    

res = model.invoke('what happened in switzerland today')

print(res.content)