# not sending to any llm ...coz it would take to much token and ill hit the rate limit
# disadvantage of load--> takes to much time to load only 3 pdfs...coz its getting stored in memory i.e RAM....what if we had say 100 pdf...tab toh bhot time chala jaayega...therefore we use something called as lazy loading
# for more differences refer to the image in this same directory 

from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader(
    path='Data',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()


for document in docs:
    print(document)