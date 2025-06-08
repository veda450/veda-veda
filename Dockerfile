# Use an official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Flask
RUN pip install flask

# Expose the default Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]