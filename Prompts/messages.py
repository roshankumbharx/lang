from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint(model= 'openai/gpt-oss-120b')


# model = ChatHuggingFace(llm = llm)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

messages = [
    SystemMessage(content='You are a professional assistant'),
    HumanMessage(content='Tell me about langChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
