
![Logo](https://blog.holbertonschool.com/wp-content/uploads/2021/05/cropped-Fichier-16.png)


# HBNB Clone

This project is a backend clone of the Holberton B&B (HBNB) web application. The application is built using Flask and provides RESTful APIs for managing users and places. It also includes a Docker configuration to containerize the application for consistent deployment across different environments.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Diagram](#Diagram)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Dockerization](#dockerization)
## Features

- Create, read, update, and delete (CRUD) operations for users and places.
- RESTful API design.
- Containerized using Docker with Alpine Linux and Gunicorn for scalability and performance.
- Persistent data storage using Docker volumes.

## Requirements

- Python 3.8+
- Flask
- Docker

## Flowchart


![Logo](https://ibb.co/PzKnxXV)


## Setup and Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/OussemaTurki0/holbertonschool-hbnb.git
    cd holbertonschool-hbnb
    ```

2. **Install dependencies:**

    Create and activate a virtual environment (optional):

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

    Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file and add the necessary environment variables:

    ```sh
    touch .env
    echo "FLASK_ENV=development" >> .env
    echo "APP_PORT=5000" >> .env
    ```

## Running the Application

1. **Run the Flask application:**

    ```sh
    flask run
    ```

## API Endpoints

### Users

- **Create a new user:**

    ```http
    POST /users
    ```

    **Request body:**

    ```json
    {
        "email": "user@example.com",
        "first_name": "First",
        "last_name": "Last"
    }
    ```

    **Response:**

    ```json
    {
        "id": "user_id",
        "email": "user@example.com",
        "first_name": "First",
        "last_name": "Last"
    }
    ```

- **Get all users:**

    ```http
    GET /users
    ```

    **Response:**

    ```json
    [
        {
            "id": "user_id",
            "email": "user@example.com",
            "first_name": "First",
            "last_name": "Last"
        },
        ...
    ]
    ```

- **Get a specific user:**

    ```http
    GET /users/{user_id}
    ```

    **Response:**

    ```json
    {
        "id": "user_id",
        "email": "user@example.com",
        "first_name": "First",
        "last_name": "Last"
    }
    ```

- **Update a user:**

    ```http
    PUT /users/{user_id}
    ```

    **Request body:**

    ```json
    {
        "email": "newemail@example.com",
        "first_name": "NewFirst",
        "last_name": "NewLast"
    }
    ```

    **Response:**

    ```json
    {
        "id": "user_id",
        "email": "newemail@example.com",
        "first_name": "NewFirst",
        "last_name": "NewLast"
    }
    ```

- **Delete a user:**

    ```http
    DELETE /users/{user_id}
    ```

### Places

- **Create a new place:**

    ```http
    POST /places
    ```

    **Request body:**

    ```json
    {
        "name": "Place Name",
        "description": "Place Description"
    }
    ```

    **Response:**

    ```json
    {
        "id": "place_id",
        "name": "Place Name",
        "description": "Place Description"
    }
    ```

- **Get all places:**

    ```http
    GET /places
    ```

    **Response:**

    ```json
    [
        {
            "id": "place_id",
            "name": "Place Name",
            "description": "Place Description"
        },
        ...
    ]
    ```

- **Get a specific place:**

    ```http
    GET /places/{place_id}
    ```

    **Response:**

    ```json
    {
        "id": "place_id",
        "name": "Place Name",
        "description": "Place Description"
    }
    ```

- **Update a place:**

    ```http
    PUT /places/{place_id}
    ```

    **Request body:**

    ```json
    {
        "name": "New Place Name",
        "description": "New Place Description"
    }
    ```

    **Response:**

    ```json
    {
        "id": "place_id",
        "name": "New Place Name",
        "description": "New Place Description"
    }
    ```

- **Delete a place:**

    ```http
    DELETE /places/{place_id}
    ```

## Dockerization

1. **Create a `Dockerfile`:**

    ```dockerfile
    # Use an appropriate base image
    FROM python:3.8-alpine

    # Set environment variables
    ENV FLASK_APP=app.py
    ENV FLASK_RUN_HOST=0.0.0.0
    ENV APP_PORT=5000

    # Install dependencies
    COPY requirements.txt requirements.txt
    RUN pip install -r requirements.txt

    # Copy the application code
    COPY . .

    # Expose the port the app runs on
    EXPOSE $APP_PORT

    # Run the Flask application with Gunicorn
    CMD ["gunicorn", "--bind", "0.0.0.0:$APP_PORT", "app:app"]
    ```

2. **Build the Docker image:**

    ```sh
    docker build -t hbnb-clone .
    ```

## Authors

- Ghofrane Amemi
- Turki Oussema
