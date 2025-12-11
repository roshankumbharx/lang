from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document = ['who is america','who is sacha baron cohen','Techmology,aight!Respekt']

vector = embedding.embed_documents(document)

print(vector)