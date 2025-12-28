from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGroq(model='llama-3.1-8b-instant')

prompt = PromptTemplate(
    template='who is {person}',
    input_variables=['person']
)

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'person':'geoffrey hinton'})

print(res)