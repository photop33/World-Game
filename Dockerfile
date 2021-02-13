FROM python:latest
COPY . "C:\Users\l1313\PycharmProjects\pythonProject9"
RUN pip install flask
CMD [ "python", MainScore.py" ]

CMD [ "python" , "/MainScore.py"]



