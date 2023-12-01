FROM python:3.11
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "Scraping.py"]
