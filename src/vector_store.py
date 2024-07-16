import os
import sys
import pandas as pd

sys.path.append("../")

from model import embeddings
from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant

from config import QDRANT_HOST, QDRANT_PORT, DOCUMENT_PATHS

def build_vector_store(collection_name='MyCollection'):
    # Ensure DOCUMENT_PATHS points to the folder containing CSV files
    document_folder = DOCUMENT_PATHS
    
    answers = []
    
    # Iterate through all CSV files in the specified directory
    for filename in os.listdir(document_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(document_folder, filename)
            df = pd.read_csv(file_path)

            # Clean the 'Answer' column from special characters
            df['Answer'] = df['Answer'].str.replace('\u200b', '', regex=False)
            df['Answer'] = df['Answer'].str.replace('\xa0', '', regex=False)
            df['Answer'] = df['Answer'].str.replace('"', '', regex=False)

            # Append answers to the list
            answers.extend(df['Answer'].tolist())

    # Initialize the Qdrant client
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
    # Define the collection name
    collection_name = collection_name
    
    # Create a Qdrant vector store
    qdrant = Qdrant(client, collection_name, embeddings)
    vectorstore = qdrant.from_texts(
        answers, embeddings
    )

    print("Done build vector store!")
    return vectorstore
