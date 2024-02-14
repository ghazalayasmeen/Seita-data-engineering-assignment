FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run main.py when the container launches
CMD ["uvicorn", "seita_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
