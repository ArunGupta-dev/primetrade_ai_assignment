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

## Testing Role-Based Access Control (RBAC)

The system distinguishes between **Analysts** (Normal Users) and **Head Traders** (Admins/Staff). To test both roles without registering multiple separate accounts manually, the automated setup scripts (both Docker and the shell script) will automatically generate a Superuser account.

### Step-by-Step: Promoting a User to Head Trader (Admin)

1. **Log in to the Django Admin Panel:**
   * Open your browser and navigate to: `http://localhost:8000/admin/`
   * Log in using the auto-generated credentials:
     * **Username:** `admin`
     * **Password:** `admin1234`

2. **Create or Locate a User Account:**
   * Click on **Users** under the *Authentication and Authorization* section.
   * If you have already registered an account via the frontend dashboard, find that user's email/username in the list.
   * If not, click **Add User** in the top right to create a new analyst account.

3. **Elevate Privileges to Head Trader:**
   * Click on the user profile you want to promote.
   * Scroll down to the **Permissions** section.
   * Check the box for **Staff status (`is_staff`)**. This designation grants the user Head Trader privileges across the REST API.
   * Click **Save** at the bottom of the page.

4. **Verify on the Frontend Dashboard:**
   * Go back to your frontend dashboard (`http://localhost:8000/home/`).
   * Log in with the newly promoted user's credentials.
   * The user will now have global read/write access to view, edit, or delete all platform trade notes rather than just their own.

### Custom Superuser Creation (Optional)
If you are running the project manually or prefer to create a custom superuser, ensure your virtual environment is active and run the following command from the `primetrade_ai` directory:
```bash
python manage.py createsuperuser



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


