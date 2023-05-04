#FROM selenium/standalone-chrome
FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /app
COPY . app
WORKDIR app
CMD ["python3", "BotTelegram.py"]
#CMD ["pytest", "-s", "test_PK.py"]
#docker run selenium/standalone-chrome
