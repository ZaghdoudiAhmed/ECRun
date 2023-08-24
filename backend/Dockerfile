# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
