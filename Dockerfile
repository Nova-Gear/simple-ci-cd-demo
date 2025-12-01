FROM python:3.12-slim

WORKDIR /app
COPY app/ /app

# Optional: install dependencies kalau ada
# RUN pip install -r requirements.txt

# Jalankan main.py, lalu terus stay alive (misal sleep infinity)
CMD ["sh", "-c", "python main.py && tail -f /dev/null"]
