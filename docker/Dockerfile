FROM python:3.11-alpine

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py .

ENV REDIS_URL=redis://redis:6379