# Tells Docker which base image to start with -> python 3.12 (lite version based on Debian Bookworm - Linux)
FROM python:3.12-slim-bookworm 

# Environment variables
# Do not write .pyc files (not needed in Docker)
ENV PYTHONDONTWRITEBYTECODE=1  
# Send all output directly to terminal, without buffering (helps to see logs in real-time)
ENV PYTHONUNBUFFERED=1      

# Set the working directory
WORKDIR /app

# Install system dependencies if needed (e.g., for psycopg)
# RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client && rm -rf /var/lib/apt/lists/*
# (Note: Using psycopg[binary] often avoids needing system deps)

# Install Python dependencies
# Upgrade pip first
RUN pip install --upgrade pip 
# Copy only requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Define the command to run the application using Gunicorn
# Replace 'myproject.wsgi:application' with your actual project's WSGI entry point
CMD ["gunicorn", "stellar_care.wsgi:application", "--bind", "0.0.0.0:8000"]