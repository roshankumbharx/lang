from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


loader = TextLoader('DocumentLoaders\git commands.txt',encoding='utf-8')

docs=loader.load()

print('page_content:',docs[0].page_content)
print('metadata:',docs[0].metadata)

print(type(docs))
print(type(docs[0]))


prompt = PromptTemplate(
    template='ask 5 questions from {text}',
    input_variables=['text']
)

model = ChatGroq(model='openai/gpt-oss-120b')

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'text':docs[0].page_content})

print(res)

