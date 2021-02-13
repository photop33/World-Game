FROM python:latest
COPY MainScore.py /
COPY Utils.py / 

RUN pip install flask
CMD [ "python", "MainScore.py" ]




