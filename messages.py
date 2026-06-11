from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ('system','You are a helpful AI assistant. Chat as an assistance and help the user resolve his query'),
    ('human','{query}')],
    input_variables = ['query']
)

