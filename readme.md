# Prime Trade AI - Backend Engineering Assignment

A scalable REST API with Role-Based Access Control (RBAC), built with Django REST Framework, featuring a Vanilla JS frontend dashboard for market analysts to log and manage trading intelligence.

## Core Features
* **JWT Authentication:** Secure login and registration using `djangorestframework-simplejwt` with automatic frontend token refreshing.
* **Role-Based Access Control (RBAC):** * **Analysts (Normal Users):** Can only view, create, edit, and delete their own Trade Notes.
    * **Head Traders (Admins):** Have global read/write access to all platform notes for intelligence aggregation.
* **Trade Notes CRUD:** Full REST API mapping for secondary entity creation with UUID primary keys.
* **Interactive Dashboard:** A glass-morphic, Vanilla JS frontend to demonstrate API functionality and role-based UI rendering.
* **API Versioning & Documentation:** Endpoints routed through `/api/v1/` and documented via Swagger/OpenAPI.

## Tech Stack
* **Backend:** Python 3, Django, Django REST Framework
* **Database:** SQLite (Development) -> Ready for PostgreSQL
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (ES6+), Fetch API
* **Security:** Argon2/PBKDF2 Password Hashing, JWT

## Local Setup & Usage Instructions

You can run this project using either the provided shell script, manual setup, or Docker. 

### Method 1: Automated Shell Script (Mac/Linux)
The repository includes a setup script that automatically creates a virtual environment, installs dependencies, applies migrations, and starts the server.

1. Clone the repository and navigate to the project root.
2. Make the script executable:
   chmod +x setup_run_server.sh
3. Run the script:
   ./setup_run_server.sh

### Method 2: Manual Setup (Windows/Mac/Linux)
1. Clone the repository and create a virtual environment:
   python -m venv env
2. Activate the virtual environment:
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Navigate into the Django project directory where manage.py is located:
   cd primetrade_ai
5. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
6. Start the server:
   python manage.py runserver

### Method 3: Docker
If you have Docker installed, you can build and run the application in an isolated container. The Dockerfile is already configured to handle the internal directory structure.

1. Build the image:
   docker build -t primetrade:latest .
2. Run the container:
   docker run -p 8000:8000 primetrade:latest




## API Documentation
The API is fully documented using Swagger/OpenAPI via `drf-spectacular`. Once the server is running, you can explore and test the endpoints interactively:
* **Swagger UI:** `http://localhost:8000/api/schema/swagger-ui/`
* **Redoc:** `http://localhost:8000/api/schema/redoc/`

## Scalability & Production Readiness Note
While this repository is configured for immediate local evaluation, the architecture is designed with production-grade scalability in mind:

* **Database Scaling:** Currently utilizing SQLite for frictionless local setup. Because data access is abstracted through the Django ORM, migrating to a robust RDBMS like **PostgreSQL** in production requires minimal effort (updating the `DATABASES` configuration and provisioning the instance).
* **Caching Strategy (Future Implementation):** To meet the assignment deadline, an in-memory cache was omitted. If built for production, **Redis** would be integrated to cache high-read endpoints (e.g., the global notes feed for Head Traders) and to manage JWT token blocklists, significantly reducing database I/O.
* **Microservices & Load Balancing:** The application is completely decoupled from the frontend. By utilizing Docker, the backend can be deployed as a stateless container across a Kubernetes cluster or AWS ECS. Traffic would be routed through a reverse proxy (like Nginx) and an application load balancer to distribute requests across multiple Gunicorn/Uvicorn worker instances.

## Security & Data Validation
* **Input Sanitization:** All incoming request payloads are strictly validated and sanitized using Django REST Framework Serializers. Extraneous fields are stripped, and type-checking prevents injection attacks.
* **Authentication Security:** The API utilizes stateless JWTs. Passwords are never stored in plain text; they are secured using Django's native PBKDF2 password hasher before hitting the database.


