FROM python:latest
ADD . "C:\Users\l1313\PycharmProjects\pythonProject9"


RUN pip install flask
RUN echo %cd%
CMD [ "python", "MainScore.py" ]



