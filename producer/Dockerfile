# Use the official python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy your app files
COPY . /app

# Install all required dependencies
RUN pip install --no-cache-dir kafka-python faker loguru

# Run your python file
CMD ["python", "producer.py"]
