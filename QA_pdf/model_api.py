from llama_index.llms.gemini import Gemini
from exception import customexception
from logger import logging
import sys
import os

def load_gemini_model():
    try:
        api_key = os.getenv("GEMINI_API_KEY")  # READ AT RUNTIME

        if not api_key:
            raise ValueError("Gemini API key not found")

        logging.info("Gemini model loaded successfully")

        return Gemini(
            model="models/gemini-2.5-flash",
            api_key=api_key
        )

    except Exception as e:
        logging.info("Error occurred while loading model")
        raise customexception(e, sys)
