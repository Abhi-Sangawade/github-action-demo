FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY ai_agent.py .

EXPOSE 5000

CMD ["python", "app.py"]