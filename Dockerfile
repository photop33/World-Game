FROM python:latest
COPY MainScore.py /
RUN pip install flask
CMD [ "python", "\MainScore.py" ]




