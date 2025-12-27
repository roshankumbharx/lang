from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

from dotenv import load_dotenv


load_dotenv()

# model = ChatGroq(model='llama-3.1-8b-instant')
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

class Person(BaseModel):
    name:str=Field(description='name of the person')
    age:int=Field(gt=18,description='age of the person')
    city:str=Field(description='name of the city of the person')
    
    
parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(
    template='give me name,age and city of an {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

res = chain.invoke({'place':'english'})

print(res)