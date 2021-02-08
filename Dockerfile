FROM python:latest
ADD MainScore.py "C:\Users\l1313\PycharmProjects\pythonProject9\app"
    MemoryGame.py "C:\Users\l1313\PycharmProjects\pythonProject9"


RUN pip install flask

CMD [ "python", "./MainScore.py" ]



