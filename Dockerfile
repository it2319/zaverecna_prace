FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser --system --group app \
    && mkdir -p /app/data \
    && chown -R app:app /app/data \
    && chmod +x /app/docker-entrypoint.sh

USER app

EXPOSE 8000

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "config.wsgi:application"]