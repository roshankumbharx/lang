from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id='openai/gpt-oss-120b',
                          task="text-generation",
                          max_new_tokens=1,temperature=0.7)
                    
models=ChatHuggingFace(llm=llm)

res = models.invoke('write me a poem like emily dickinson')

print(res.content)