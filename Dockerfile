# ---------- Stage 1: frontend build ----------
FROM node:20-alpine AS frontend-builder

WORKDIR /app/frontend

COPY frontend/package*.json ./

RUN npm ci

COPY frontend .

RUN npm run build


# ---------- Stage 2: backend runtime ----------
FROM python:3.12-slim

WORKDIR /app

COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

COPY . .

COPY --from=frontend-builder /app/staticfiles ./staticfiles
COPY --from=frontend-builder /app/frontend/src/asset/ ./media/

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]