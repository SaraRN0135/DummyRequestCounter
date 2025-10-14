# Use a lightweight Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app folder into the container
COPY ./app ./app

# Environment variables for FastAPI
ENV REDIS_HOST=redis
ENV REDIS_PORT=6379

# Expose FastAPI port
EXPOSE 8000

# Command to run the API
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]
