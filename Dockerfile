FROM python:latest
COPY MainScore.py /
COPY Utils.py / 
COPY Score.py / 

RUN pip install pymysql
RUN pip install flask
RUN pip install selenium
RUN mkdir /code
CMD [ "python", "MainScore.py" ]

EXPOSE 8777


