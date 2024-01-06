import os 
from pathlib import Path 

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/dataingestion.py",
    "src/components/datatransformation.py",
    "src/components/modeltrainer.py",
    "src/components/modelevaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.py",
    "requirements.txt",
    "requirements_dev.txt",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "pyproject.toml",
    "experiment/experiments.ipynb"
] 


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir , filename = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir , exist_ok = True)
        # logging.info(f"Creating Directory : {file_dir} for file : {filename}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path , "w") as file:
            pass 
