# Use the official Python image as the base image
FROM python:3.11.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Expose the port on which the Flask server will run
EXPOSE 8000

RUN ls

# Set the entrypoint command to start the Flask server
CMD ["gunicorn","-b 0.0.0.0:8000", "main:app"]