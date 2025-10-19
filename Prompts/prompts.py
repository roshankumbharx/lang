from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm=HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-R1',task='text-generation')

model = ChatHuggingFace(llm=llm)

print('Enter Input:')
userInput=input()
res = model.invoke(userInput)

print(res.content)