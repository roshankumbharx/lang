from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(model= 'openai/gpt-oss-120b')

model = ChatHuggingFace(llm = llm)

messages = [
    SystemMessage(content='You are a professional assistant'),
    HumanMessage(content='Tell me about langChain')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)
