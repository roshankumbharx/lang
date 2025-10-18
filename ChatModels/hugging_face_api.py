from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id='HuggingFaceH4/zephyr-7b-beta',
                          task="text-generation",
                          max_new_tokens=10)
                    
models=ChatHuggingFace(llm=llm)

res = models.invoke('what is the capital of india')

print(res.content)