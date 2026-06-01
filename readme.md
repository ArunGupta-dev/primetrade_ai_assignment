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

You can run this project using either the provided shell script or Docker. 

### Method 1: Automated Shell Script (Mac/Linux)
The repository includes a setup script that automatically creates a virtual environment, installs dependencies, applies migrations, and starts the server.

1. Clone the repository and navigate to the project root.
2. Make the script executable:
   chmod +x setup_run_server.sh
3. Run the script:
   ./setup.sh

### Method 2: Manual Setup (Windows/Mac/Linux)
1. Clone the repository and create a virtual environment:
   python -m venv env
2. Activate the virtual environment:
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start the server:
   python manage.py runserver

### Method 3: Docker
If you have Docker installed, you can build and run the application in an isolated container.

1. Build the image:
   docker build -t primetrade-api .
2. Run the container:
   docker run -p 8000:8000 primetrade-api





