from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatOllama(model='llama2')
model2 = ChatGroq(model='llama-3.1-8b-instant')

prompt1 = PromptTemplate(
    template='give me a detailed report on {topic}',
    input_variables=['topic']
)


prompt2=PromptTemplate(
    template='give me a 5 line summary on the {text}',
    input_variables=['text']
)

parser = StrOutputParser()


chain = prompt1 | model1 | parser | prompt2 | model2 | parser

res = chain.invoke({'topic':'black hole'})

print(res)

chain.get_graph().print_ascii()