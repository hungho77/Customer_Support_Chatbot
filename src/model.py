from config import GOOGLE_API_KEY
import os

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

from langchain_google_genai import GoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

llm = GoogleGenerativeAI(model="gemini-2.0-flash-exp")
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
print("Done Load Model!")