from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


url = 'https://www.flipkart.com/apple-iphone-17-pro-max-cosmic-orange-512-gb/p/itm9610ba7d9c887?pid=MOBHFN6YGCTS2WGA&lid=LSTMOBHFN6YGCTS2WGAMEXV4L&marketplace=FLIPKART&q=iphone+17&store=tyy%2F4io&srno=s_1_8&otracker=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_2_na_na_na&fm=organic&iid=29b2f982-f833-4de4-99e7-9547d0c3381d.MOBHFN6YGCTS2WGA.SEARCH&ppt=pp&ppn=pp&ssid=ycqz71mzuo0000001767315169051&qH=c9eeb2d6cc488f0b'
loader = WebBaseLoader(url)

docs = loader.load()


prompt = PromptTemplate(
    template='answer the {questions} from the following {text}',
    input_variables=['questions','text']
)

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash-lite')

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'questions':'what is the price of the product','text':docs[0].page_content})

print(res)