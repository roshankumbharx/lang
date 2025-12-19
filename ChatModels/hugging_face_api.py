from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id='HuggingFaceH4/zephyr-7b-beta',
                          task="text-generation",
                          temperature=0.7)
                    
models=ChatHuggingFace(llm=llm)

res = models.invoke('what is hugging face in short')

print(res.content)