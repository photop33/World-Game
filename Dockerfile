FROM python:latest
COPY MainScore.py "C:\Users\l1313\PycharmProjects\pythonProject9"
RUN pip install flask
CMD [ "python", MainScore.py" ]




