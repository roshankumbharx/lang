from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0)

result =  model.invoke('Write me a poem like emily dickinson')
print(result.content)