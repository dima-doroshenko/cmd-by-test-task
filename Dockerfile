FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--port", "5000", "--host", "0.0.0.0"]

