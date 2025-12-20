from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

# schema
class Review(TypedDict):
    
    summary:str
    semantic:str
    

sturctured_model = model.with_structured_output(Review)

response = sturctured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

""")

print(response)


# typeddict not supported anymore in langchain...will give an error....use pydantic instead