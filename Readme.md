# Customer_Support_Chatbot
Build a “Customer-Support Chatbot” for a bank

## Clone source
```bash
git clone https://github.com/hungho77/Customer_Support_Chatbot_Zalo.git
cd Customer_Support_Chatbot_Zalo
```

## Installation

### Python
Create a conda environment and install the requirements:
```bash
conda create -n chatbot python=3.10 -y
conda activate chatbot
pip install -r requirements.txt
```

## Create env
Create file .env (using vim) and setting environment variable

```bash 
GOOGLE_API_KEY="google api key"
DOCUMENT_PATHS="path to folder contant document as csv files"
QDRANT_HOST="localhost"
QDRANT_PORT="6333"
```
copy above environment variable into .env file and save
```bash
cd src
vi .env
```
then
```bash
cd ../
```

## Run qdrant storage
```bash
sudo docker run -d -p 6333:6333 -p 6334:6334 -v $(pwd)/qdrant_storage:/qdrant/storage qdrant/qdrant
```

## Run the application
```bash
streamlit run src/app.py
```

## Use the application
```bash
open browser with url below
Local URL: http://localhost:8501
Network URL: 
```

### Examples
[Download the demo video](assets/demo.mp4)

