
import os
import sys
import pandas as pd

sys.path.append("../")

from model import embeddings
from qdrant_client import QdrantClient
from langchain_qdrant import Qdrant
from langchain_core.documents import Document

from config import QDRANT_HOST, QDRANT_PORT, DOCUMENT_PATHS

# ...existing imports...

def build_vector_store(collection_name='MyCollection'):
    document_folder = DOCUMENT_PATHS
    documents = []
    
    # Iterate through all CSV files in the specified directory
    for filename in os.listdir(document_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(document_folder, filename)
            df = pd.read_csv(file_path)

            # Clean the 'summary' column from special characters
            df['summary'] = df['summary'].str.replace('\u200b', '', regex=False)
            df['summary'] = df['summary'].str.replace('\xa0', '', regex=False)
            df['summary'] = df['summary'].str.replace('"', '', regex=False)

            # Create Document objects with summary as content and answer as metadata
            for _, row in df.iterrows():
                doc = Document(
                    page_content=row['summary'],
                    metadata={'Answer': row['Answer'],
                              'description': row['description'],
                              'priority': row['priority'],
                              'created': row['created'],
                              'creator': row['creator']
                              ,'reporter': row['reporter'],
                              'progress': row['progress'],
                              'issuetype': row['issuetype'],
                              'status': row['status'],
                              'assignee': row['assignee'],
                              'updated': row['updated']
                              }
                )
                documents.append(doc)

    # Initialize the Qdrant client
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
    # Create a Qdrant vector store
    qdrant = Qdrant(client, collection_name, embeddings)
    vectorstore = qdrant.from_documents(
        documents,
        embeddings
    )

    print("Done build vector store!")
    return vectorstore




# import os
# import sys
# import pandas as pd

# sys.path.append("../")

# from model import embeddings
# from qdrant_client import QdrantClient
# from langchain_qdrant import Qdrant

# from config import QDRANT_HOST, QDRANT_PORT, DOCUMENT_PATHS

# def build_vector_store(collection_name='MyCollection'):
#     # Ensure DOCUMENT_PATHS points to the folder containing CSV files
#     document_folder = DOCUMENT_PATHS
    
#     answers = []
    
#     # Iterate through all CSV files in the specified directory
#     for filename in os.listdir(document_folder):
#         if filename.endswith('.csv'):
#             file_path = os.path.join(document_folder, filename)
#             df = pd.read_csv(file_path)

#             # Clean the 'Answer' column from special characters
#             df['summary'] = df['summary'].str.replace('\u200b', '', regex=False)
#             df['summary'] = df['summary'].str.replace('\xa0', '', regex=False)
#             df['summary'] = df['summary'].str.replace('"', '', regex=False)

#             # Append answers to the list
#             answers.extend(df['summary'].tolist())

#     # Initialize the Qdrant client
#     client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    
#     # Define the collection name
#     collection_name = collection_name
    
#     # Create a Qdrant vector store
#     qdrant = Qdrant(client, collection_name, embeddings)
#     vectorstore = qdrant.from_texts(
#         answers, embeddings
#     )

#     print("Done build vector store!")
#     return vectorstore, df
