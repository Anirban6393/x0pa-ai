# X0PA-AI: Predictive Model For Classifying Job Descriptions Into Categories/Titles

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

## Importable Modules & Data Files

**x0pa_ds_interview_round_2_train.xlsx** - Training Dataset used to train model<br>
**x0pa_ds_interview_round_2_test.xlsx** - Test Dataset without Job category column used to make model prediction and determine performance
**x0pa_ds_interview_round_2_test_predictions.xlsx** - Test dataset including model prediction column

**sgd_classifier.pkl** - Trained SGD classifier parameters for input data inferencing pipeline <br>
**pipe.pkl** - Sklearn pipeline used to preprocess input job description on train dataset, can be used for inference pipeline 

Inside the **nlp_module** folder, some importable modules I created worth highlighting.

**Dataprocessor.py** - Class and its methods for importing all formats of files, transformation into pivot table, normalisation

**Modelevaluator.py** - Contains class and its methods for model training, cross validation, evaluation and persistence into pickle file

I have also added __init__.py file mentioning this scripts inside this directory so that these scripts are considered as importable modules.
```
from nlp_module.Dataprocessor import *
from nlp_module.Modelevaluator import *
```

## Streamlit API
A Streamlit API to return predictions from a trained ML model, built with Python 3 and Flask-REST module.

Development set-up instructions
First, open a command line interface and clone the GitHub repo in your workspace

```
git clone https://github.com/Anirban6393/x0pa-ai.git
cd x0pa-ai
```

Once dependencies are installed, set up the requirements.txt to download required packages.
```
pip install -r requirements.txt
```
Now, run app.py python script that interfaces with end users uploading some excel file and dumping into sqlite3 database.
Upload **x0pa_ds_interview_round_2_test.xlsx** 

```
python app.py
```
Open the URL http://localhost:8501/ with your browser to view the list of job titles predicted by model for given job descriptions.

## Docker Command

Build docker image to begin with. It utilises dockerfile in the directory.
```
docker build -f Dockerfile -t app/x0pa .
```
Next, you can run the docker commands. Be sure to publish export ports for all containers to access.
``` 
docker run -p 8501:8501 -d app/x0pa
```
View all containers running.
``` 
docker ps -a 
```
Stop and kill a container.
``` 
docker container stop <container_id>/<container_name>
docker container kill <container_id>/<container_name>
```
Restart a stopped container.
``` 
docker container restart <container_id>/<container_name>  
```

Delve into a docker container. Install vim in order to download linux editor for viewing and editing files inside container directory.
```
docker exec -it <container_id>/<container_name> bash
apt-get install vim
ls -lrt
vi <filename>
```
