FROM python:latest
COPY MainScore.py /
COPY Utils.py / 
COPY Score.py / 

RUN pip install pymysql
RUN pip install flask
RUN pip install selenium
CMD [ "python", "MainScore.py" ]




