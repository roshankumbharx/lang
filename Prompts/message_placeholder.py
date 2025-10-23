from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

# chat temp

chat_template = ChatPromptTemplate([
    ('system','you are an customer support assistant'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# load chat history
chat_history =[]
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt 
prompt = chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
print(prompt)