from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableBranch,RunnablePassthrough

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='generate a detailed report on {topic} \n and start by saying this is the detailed report on {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='write a sumamry on the following {text} \n in 100 words and start by saying this is the summary',
    input_variables=['text']
)

report = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x:len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()    
)

merge_chain = report | branch_chain

res = merge_chain.invoke({'topic':'langchain'})

print(res)