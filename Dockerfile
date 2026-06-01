FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project into /app
COPY . /app/

# Change the working directory to where manage.py is located
WORKDIR /app/primetrade_ai

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
