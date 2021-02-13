FROM python:latest
COPY MainScore.py /
COPY Utils.py / 
COPY Score.py / 


RUN pip install flask
CMD [ "python", "MainScore.py" ]




