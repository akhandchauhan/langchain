import os

from model_loader import model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template
chat_template =  ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []
# load chat history
with open(os.path.join(os.path.dirname(__file__), 'chat_history.txt')) as f:
    chat_history.extend(f.readlines())

# create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':"where is my refund?"})

print(model.invoke(prompt))