# x0pa-ai

Git commands for creating github repository from local directory command line, pushing folder to created repo, deleting selective folders and commit changes

```
git init -b x0pa-ai
gh repo create x0pa-ai
git pull --set-upstream origin x0pa-ai

git rm -r --cached folder
git commit -m "Removed folder from repository"
git push origin main
```
