FROM python:3.9-slim

# Install nano
RUN apt-get update && apt-get install -y nano && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy everything 
COPY . . 

# Define a volume : I will map this volume in deployment yaml with the actual path
VOLUME ["/app/data"]

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
