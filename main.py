import os
import openai
import sys
#from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from pypdf import PdfReader

sys.path.append('../..')
openai.api_key = os.environ["OPENAI_API_KEY"]
PATH = os.environ["LANGCHAIN_TESTING_PATH"]

loader1 = TextLoader(f"{PATH}/Sample_TXT.txt")

index = VectorstoreIndexCreator().from_loaders([loader1])

while True:
    print("\nEnter your query or type 'done' to quit.")
    user_query = input("Query: ")
    if user_query == 'done':
        break
    else:
        index.query(user_query)
        # index.query_with_sources(user_query) # useful when querying multiple documents

'''
filename = "/Users/hashim.bukhtiar/Desktop/Technical Roadmap/LangChainTesting/Sample_PDF.pdf"
openai.api_key = "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"
loader = PyPDFLoader(filename)
reader = PdfReader(filename)
page = reader.pages[0]
text = page.extract_text()
print(text)
'''