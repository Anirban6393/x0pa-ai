# X0PA-AI: Predictive Model For Classifying Job Descriptions Into Categories/Titles

## Importable Modules

Inside the **nlp_module** folder, some importable modules I created worth highlighting.

**Dataprocessor.py** - Class and its methods for importing all formats of files, transformation into pivot table, normalisation

**Modelevaluator.py** - Contains class and its methods for model training, cross validation, evaluation and persistence into pickle file

I have also added __init__.py file mentioning this scripts inside this directory so that these scripts are considered as importable modules.
```
from nlp_module.Dataprocessor import *
from nlp_module.Modelevaluator import *
```

## Creating Git Repo, Commiting Changes

Git commands for creating github repository from local directory command line, pushing folder to created repo, deleting selective folders and commit changes

```
git init -b x0pa-ai
gh repo create x0pa-ai
git pull --set-upstream origin x0pa-ai

git rm -r --cached folder
git commit -m "Removed folder from repository"
git push origin main
```

## Rest API
A REST API to return predictions from a trained ML model, built with Python 3 and Flask-REST module.

Development set-up instructions
First, open a command line interface and clone the GitHub repo in your workspace

```
PS > git clone https://github.com/Anirban6393/x0pa-ai.git
PS > cd x0pa-ai
```

Once dependencies are installed, set up the requirements.txt to download required packages.
```
(venv) PS > pip install -r requirements.txt
```
Now, run app.py python script that interfaces with end users uploading some excel file and dumping into sqlite3 database.
Upload x0pa_ds_interview_round_2_test.xlsx 

```
(venv) PS > python app.py
```
Open the URL http://127.0.0.1:1000/ with your browser to view the list of job titles predicted by model for given job descriptions.

## Docker Command

Build docker image to begin with. It utilises dockerfile in the directory.
```
docker build -t akc/test-nlp .
```
Next, you can run the docker commands. Be sure to publish export ports for all containers to access.
``` 
docker run -it akc/test-nlp
docker run -P -d akc/test-nlp
```
