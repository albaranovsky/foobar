FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

CMD ["gunicorn", "--bind", ":8000", "--access-logfile", "-", "app:app"]
