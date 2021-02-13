FROM python:latest
ADD MainScore.py /
RUN pip install flask
CMD [ "python", "\MainScore.py" ]




