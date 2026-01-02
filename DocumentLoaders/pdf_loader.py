from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.pdf import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()


loader = PyPDFLoader('./Data/Time_and_Work_Formulas_Practice.pdf')

docs = loader.load()

print(docs[0].page_content)
print('document lengh:',len(docs),'\n')

model = ChatGroq(model='groq/compound')

parser=StrOutputParser()

prompt = PromptTemplate(
    template='ask me questions bases on {text}',
    input_variables=['text']
)

chain = prompt | model | parser


res = chain.invoke({'text':docs[0].page_content})
print(res)
