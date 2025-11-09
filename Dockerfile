# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Create log dir & set permissions
RUN mkdir -p /var/log && touch /var/log/counter.log && chown -R root:root /var/log

ENV PORT=5000
EXPOSE 5000

CMD ["python", "app.py"]
