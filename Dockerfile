FROM python:3.11
LABEL authors="Michael Jordan"
ADD . /app
WORKDIR /app

RUN pip install  -r requirements.txt

VOLUME /app/db

CMD ["python", "main.py"]