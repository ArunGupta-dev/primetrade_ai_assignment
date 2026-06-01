FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_PASSWORD=admin1234
ENV DJANGO_SUPERUSER_EMAIL=admin@primetrade.ai

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

WORKDIR /app/primetrade_ai

EXPOSE 8000

CMD sh -c "python manage.py migrate && python manage.py createsuperuser --noinput || true && python manage.py runserver 0.0.0.0:8000"
