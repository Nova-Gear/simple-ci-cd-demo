# Gunakan base image Python ringan
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Copy file requirements dulu untuk caching layer
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh folder app
COPY app/ .

# Expose port Flask
EXPOSE 8000

# Jalankan aplikasi
CMD ["python", "main.py"]
