from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

prompt1 = PromptTemplate(
    template='you are a twitter post expert generate a post on {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='you are an linkedin expert generate a post on {topic}',
    input_variables=['topic']
)

parser= StrOutputParser()


# parallel_chain = RunnableParallel({
#     'twitter':RunnableSequence(prompt1,model,parser),
#     'linkedin':RunnableSequence(prompt2,model,parser)
# })

parallel_chain = RunnableParallel({
    'twitter':prompt1 | model | parser,
    'linkedin':prompt2 | model | parser
})

res = parallel_chain.invoke({'topic':'AI'})

print(res)
print(res['twitter'])
print(res['linkedin'])