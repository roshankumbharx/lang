from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch,RunnableLambda


load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant')

parser1 = StrOutputParser()


class Feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='give the sentiment of the feedback')
    
    
parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback into positive or negative {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


prompt2=PromptTemplate(
    template='give an appropriate response to this positive feedback {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='give an appropriate response to this negative feedback {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser1),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser1),
    RunnableLambda(lambda x:'could not find sentiment')
)

chain = classifier_chain | branch_chain

res = chain.invoke({'feedback':'This watch did not live up to my expectations'})

print(res)

chain.get_graph().print_ascii()