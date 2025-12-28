from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class Review(BaseModel):
    summary:str
    sentiment:str
    

structured_model = model.with_structured_output(Review)


res = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
""")

print(res)