# Secure REST API with JWT Authentication

This project is a secure, containerized REST API built with Python and Flask. It provides user registration, login, and a protected endpoint using JSON Web Tokens (JWTs) for stateless authentication.

## Features

- User registration with secure password hashing using **bcrypt**.
- User login that returns a signed JWT.
- A protected `/profile` endpoint that requires a valid JWT for access.
- Fully containerized with **Docker** for consistent deployment.

## Technologies Used

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Bcrypt
- **Authentication:** PyJWT
- **Database:** SQLite
- **Containerization:** Docker

## Setup and Installation

To run this project, you will need Docker installed on your machine.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/paintkid/secure-login-service.git
    cd secure-login-service
    ```

2.  **Create an environment file:**
    Create a file named `.env` and add your secret key:

    ```
    SECRET_KEY='your-strong-random-secret-key-goes-here'
    ```

3.  **Build the Docker image:**

    ```bash
    docker build -t secure-login-service .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 secure-login-service
    ```
    The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Register a New User

- **URL:** `/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "newuser",
    "password": "password123"
  }
  ```
- **Success Response:**
  ```json
  {
    "success": "User successfully created"
  }
  ```

### Login an Existing User

- **URL:** `/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "newuser",
    "password": "password123"
  }
  ```
- **Success Response:**
  ```json
  {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
  ```

### Get User Profile (Protected)

- **URL:** `/profile`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer <your-jwt-token>`
- **Success Response:**
  ```json
  {
    "id": 1,
    "username": "newuser"
  }
  ```
