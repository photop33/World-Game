FROM python:latest
COPY MainScore.py /
COPY Utils.py / 
COPY Score.py / 


RUN pip install flask
RUN pip install get
CMD [ "python", "MainScore.py" ]




