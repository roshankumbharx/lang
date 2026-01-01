# runnable lambda can conver any python funx into runnable

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

model = ChatGroq(model='openai/gpt-oss-120b')

prompt1=PromptTemplate(
    template='tell me a dark joke about {topic}',
    input_variables=['topic'] 
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)


def word_count(text):
    return len(text.split())


parallelchain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'length':RunnableLambda(word_count)
}
)

final_chain=RunnableSequence(joke_gen_chain,parallelchain)

res = final_chain.invoke({'topic':'society'})

print(res)
