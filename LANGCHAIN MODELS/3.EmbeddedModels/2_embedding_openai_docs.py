from langchain import OpenAIEmbeddings
from dotenv import load_dotenv 

load_dotenv()

documents = [
    "hello",
    "hello bro, hows is this?"
]
embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions = 32)

result = embedding.embed_documents(documents)

print(str(result))