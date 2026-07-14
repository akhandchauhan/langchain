from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from model_loader import model

messages = [
    SystemMessage(content = 'You are a senior software engineer'),
    HumanMessage(content = 'Tell me about Langchain')
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)