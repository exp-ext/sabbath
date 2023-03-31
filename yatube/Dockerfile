# pull official base image
FROM python:3.7-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

CMD ["gunicorn", "yatube.wsgi:application", "--bind", "0.0.0.0:8000" ]
