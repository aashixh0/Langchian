from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-3.5-flash')

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Explain the role of a {job_role} and what are the skills required for this job profile in brief',
    input_variables=['job_role']

)

chain = prompt | model | parser

result = chain.invoke({'job_role':'Product Manager'})

print(result)