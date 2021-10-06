# x0pa-ai

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
A RESTful API to return predictions from a trained ML model, built with Python 3 and Flask-RESTX

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
