from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint(model= 'openai/gpt-oss-120b')

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

chat_history=[
    SystemMessage(content='You are an helpful assistant who ans only in short unless said in detail or something like that')
]

while True:
    userInput = input('You:')
    chat_history.append(HumanMessage(content=userInput))
    if userInput=='exit':
        break
    res= model.invoke(userInput)
    print('AI: ',res.content)
    chat_history.append(AIMessage(content=res.content))

print(chat_history)