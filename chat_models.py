from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-pro-preview", temperature=0.9)

response = model.invoke("Explain what is the Langchain")

# Extract text from the content list
text_response = response.content[0]['text']
print(text_response)