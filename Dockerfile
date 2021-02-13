FROM python:latest
ADD . "C:\Users\l1313\.jenkins\workspace\Game-World\app"
RUN pip install flask
CMD [ "python", "/MainScore.py" ]




