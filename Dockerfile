FROM python:3.12-slim

WORKDIR /app

# Установка node
RUN apt-get update && apt-get install -y nodejs npm

COPY . .

WORKDIR /app/frontend

RUN npm install
RUN npm run build

WORKDIR /app

RUN pip install --no-cache-dir -r req.txt

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]