from langchain_ollama import ChatOllama

llm = ChatOllama(model='llama2')

response = llm.invoke('what is ai')

print(response.content)