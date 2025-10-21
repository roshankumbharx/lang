from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(model= 'openai/gpt-oss-120b')

model = ChatHuggingFace(llm=llm)

while True:
    userInput = input('You:')
    if userInput=='exit':
        break
    res= model.invoke(userInput)
    print('AI: ',res.content)