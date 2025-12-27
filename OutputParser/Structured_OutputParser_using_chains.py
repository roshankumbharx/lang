from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

model = ChatGroq(model='llama-3.1-8b-instant')

# jo schema mein o/p chahiye ...uska schema banana padta hai...aur wo banate hai Response Schema ka use karke

schema = [
    ResponseSchema(name='fact_1',description='fact 1 about topic'),
    ResponseSchema(name='fact_2',description='fact 2 about topic'),
    ResponseSchema(name='fact_3',description='fact 3 about topic')
]


parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give me 3 facts about {topic} {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain = template | model | parser

res = chain.invoke({'topic':'black hole'})

print(res)