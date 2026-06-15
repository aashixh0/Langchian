from langchain_community.document_loaders import TextLoader

file_path = 'textfile.txt'

loader = TextLoader(
    file_path = file_path,

)

docs = loader.load()
