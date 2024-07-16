import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
# print(dotenv_path)
load_dotenv(dotenv_path)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
DOCUMENT_PATHS = os.environ.get("DOCUMENT_PATHS")
QDRANT_HOST = os.environ.get("QDRANT_HOST")
QDRANT_PORT = os.environ.get("QDRANT_PORT")