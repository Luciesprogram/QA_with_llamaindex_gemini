from pathlib import Path
import os 


list_of_paths = [
    "QA_pdf/data_ingestion.py",
    "QA_pdf/model_api.py",
    "QA_pdf/__init__.py",
    "QA_pdf/embeddings.py",
    "logger.py",
    "App.py",
    "exception.py",
    "Experiments/experiments.ipynb"
]


for filepath in list_of_paths:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath) or os.path.getsize(filepath)== 0):
        with open(filepath, 'w') as f:
            pass



