FROM python:3.12-slim

WORKDIR /app

COPY requirements requirements

RUN pip install -r requirements/dev.txt

COPY . .

CMD ["python3", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]