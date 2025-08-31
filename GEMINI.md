# GEMINI.md

## Project Overview

This project is a Django REST API for an insurance application. It includes functionalities for managing users, policies, clients, agents, and insurance companies. The project is set up with Django REST Framework for building the API, `djangorestframework-simplejwt` for JWT authentication, and `drf-spectacular` for API documentation.

### Key Technologies

*   **Backend:** Django, Django REST Framework
*   **Authentication:** JWT (djangorestframework-simplejwt)
*   **API Documentation:** drf-spectacular
*   **Dependencies:**
    *   `django`
    *   `django-cors-headers`
    *   `djangorestframework`
    *   `djangorestframework-simplejwt`
    *   `drf-spectacular[sidecar]`
    *   `gunicorn`

### Architecture

The project follows a standard Django architecture:

*   **`insurance-be/`:** The main project directory containing settings, and root URL configuration.
*   **`apps/`:** A directory containing individual Django apps:
    *   **`users`:** Manages user authentication and user models.
    *   **`policy`:** Manages insurance policies, clients, agents, and related data.
*   **`manage.py`:** The Django command-line utility for administrative tasks.
*   **`pyproject.toml`:** Defines project dependencies.

## Building and Running

### Prerequisites

*   Python >= 3.12
*   `uv` 

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd insurance-be
    ```
2.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt 
    ```
    or
    ```bash
    pip install -r requirements.txt
    ```

### Running the Development Server

1.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```
2.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
The application will be available at `http://127.0.0.1:8000`.

### API Documentation

The API documentation is available at the following endpoints:

*   **Swagger UI:** `/api/docs/`
*   **ReDoc:** `/api/redoc/`
*   **Schema:** `/api/schema/`

## Development Conventions

### Code Style

The project appears to follow the standard Django code style.

### Testing

The project includes a `tests.py` file in the `apps/policy` directory and a `tests` directory in the `apps/users` directory, indicating that tests are part of the development process. To run the tests, use the following command:

```bash
python manage.py test
```

### Commits

Commit messages should be clear and concise, describing the changes made.

### Considerations

Always assume the server is running
Do not run tests files