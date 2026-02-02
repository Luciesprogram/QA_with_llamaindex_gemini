from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import VectorStoreIndex, Settings

from QA_pdf.data_ingestion import load_data
from QA_pdf.model_api import load_gemini_model
from exception import customexception
from logger import logging
import sys
import os

from dotenv import load_dotenv

load_dotenv()
gemini_api = os.getenv('GEMINI_API')

def loading_gemini_embedding(model,documents):
    try:
        logging.info("Starting loading gemini embedding model")
        embed_model = GeminiEmbedding(model_name="models/gemini-embedding-001")

        # Global Settings API
        Settings.llm = model
        Settings.embed_model = embed_model
        Settings.chunk_size = 200
        Settings.chunk_overlap = 30


        logging.info("Creating Vecotstore Index")
        index = VectorStoreIndex.from_documents(documents)

        # Persist index
        index.storage_context.persist()

        logging.info("Vectors created and persisted successfully")

        return index.as_query_engine()
    except Exception as e:
        logging.error("Error in download_gemini_embedding", exc_info=True)
        raise customexception(e,sys)