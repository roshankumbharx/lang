from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

prompt1=PromptTemplate(
    template='tell me a dark joke about {topic}',
    input_variables=['topic'] 
)

prompt2 = PromptTemplate(
    template='explain the joke {text}',
    input_variables=['text']
)

parser = StrOutputParser()


# RunnableSequence is the same as the '|' operator 

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

res = chain.invoke({'topic':'python'})

print(res)

