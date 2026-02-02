from llama_index.core import SimpleDirectoryReader
import sys,tempfile,os
from exception import customexception
from logger import logging


    
    

def load_data(uploaded_file):
    try:
        logging.info("Data Loading started")
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            logging.info("Data loading completed")
            return SimpleDirectoryReader(tmp_dir).load_data()
        
    except Exception as e:
        logging.info("Exception occured while loading data")
        raise customexception(e,sys)
    
