FROM python:3.11
LABEL authors="Michael Jeffrey Jordan"
ADD . /app
WORKDIR /app

RUN pip install  -r requirements.txt

CMD ["python", "main.py"]