FROM python:3.7-slim-buster

WORKDIR /opt/app
VOLUME /opt/app

COPY . . 

RUN pip install -r requirements.txt
EXPOSE 1000:1000


CMD ["python","./app.py"]



