FROM python:latest
COPY MainScore.py /C:\Users\l1313\.jenkins\workspace\Game-World
RUN pip install flask
CMD [ "python", "\MainScore.py" ]




