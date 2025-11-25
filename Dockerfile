FROM python:3.10-slim

WORKDIR /app

COPY src/ ./src
COPY todo_data.json .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "src/todo.py"]
