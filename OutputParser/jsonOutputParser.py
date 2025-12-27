from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

parser = JsonOutputParser()

template= PromptTemplate(
    template='Give me name, age and location of a fictional character {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt = template.invoke({})

res = model.invoke(prompt)

print(res)
final_res = parser.parse(res.content)

print(final_res)