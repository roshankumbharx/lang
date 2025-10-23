# used to create dynamic prompts  

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','you a are en expert in {domain}'),
    ('human','write me a {topic}')
])


prompt = chat_template.invoke({'domain':'poet','topic':'haiku'})

print(prompt)