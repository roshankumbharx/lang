from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser = JsonOutputParser()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

template1=PromptTemplate(template='Give me the name age and city of a fictional person \n {format_instructions}',
                         input_variables=[],
                         partial_variables={'format_instructions':parser.get_format_instructions()}

                         )

prompt = template1.format()

res = model.invoke(prompt)
final_res = parser.parse(res.content)

print(final_res)