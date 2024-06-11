#-------------------------------------------------------------------------------------------------------------------------
# We create a Dockerfile to tell Docker how to build our application into a Docker container. 
# A Docker container is like a lightweight, standalone package that contains everything our application needs to run,
# including the code, dependencies, and configuration settings. 
# The Dockerfile specifies the steps to set up our application environment inside the container,
# such as installing dependencies, configuring the application, and specifying how the application should start.
#-------------------------------------------------------------------------------------------------------------------------
# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
