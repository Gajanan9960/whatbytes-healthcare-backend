# Healthcare Backend API

This is the backend system for a healthcare application built with Django, Django REST Framework (DRF), and PostgreSQL. It allows users to register, log in, and manage patient and doctor records securely using JWT authentication.

## Prerequisites

- Python 3.x
- PostgreSQL
- Git

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your_repo_url>
   cd whatbytes-healthcare-backend
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration:**
   - Create a PostgreSQL database named `healthcare_db`.
   - Update the `DATABASES` settings in `healthcare/settings.py` or create a `.env` file from `.env.example` if configured.
   
5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

## Testing the APIs

A detailed Postman testing guide has been provided in this repository. Please refer to `postman_testing_guide.txt` for the complete list of endpoints, payloads, and instructions on how to use JWT authentication.

### Key Endpoints:
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and receive a JWT token
- `GET, POST, PUT, DELETE /api/patients/` - Patient CRUD (Authenticated)
- `GET, POST, PUT, DELETE /api/doctors/` - Doctor CRUD (Authenticated)
- `GET, POST /api/mappings/` - Patient-Doctor Mapping management
- `GET /api/mappings/<patient_id>/` - Retrieve all doctors for a specific patient
- `DELETE /api/mappings/<mapping_id>/` - Delete a specific assignment
