# StellarCare

This is a Django-based Hospital Management System that implements CRUD operations for patient records. The system allows users to create, read, update, and delete patient information. Authentication and permissions are implemented to protect sensitive operations.

## Base URL Paths

Web frontend (Django views):
```bash
/records/
```

REST API base URL:
```bash
/api/
```

## Web Frontend CRUD Operations

### 1. View All Patients
Navigate to `/records/` to see a complete list of patients.

### 2. View Patient Details
Navigate to `/records/<int:pk>/` or click on a patient's name to see detailed information of a specific patient.

### 3. Add a New Patient
Navigate to `/records/create` or click "Add Patient" to add a new patient.

### 4. Update Patient Information
Navigate to `/records/<int:pk>/update/` or clcik "Update" to update a patient's information.

### 5. Delete a Patient
Navigate to `/records/<int:pk>/delete/` or click "Delete" to remove a patient from the system.

## Setup Instructions

### 1. Clone the repository 
```powershell
git clone https://github.com/rene3phillips/stellar_care
cd stellar_care
```

### 2. Create and activate a virtual environment
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install required dependencies
```powershell
pip install -r requirements.txt
```

### 4. Google OAuth Setup

1. Go to the Google Cloud Console.
2. Create or select a project.
3. Navigate to APIs & Services > Credentials.
4. Create OAuth 2.0 Client ID credentials:
    Application type: Web application
    Authorized redirect URI:

    ```bash
    http://localhost:8000/accounts/google/login/callback/
    ```
### 5. Create a .env file 
Create a `.env` file based on `env.example` and fill in actual database credentials. 

### 6. Run Migrations
```powershell
python manage.py migrate
```

### 7. Create a superuser
```powershell
python manage.py createsuperuser
```
Follow the prompts to create a user account for the Django admin site.

### 8. Run the development server
```powershell
python manage.py runserver
```

## Testing Authentication & Permissions

### Login Testing
1. Visit http://localhost:8000/accounts/login
2. Log in with:  
    - Login credentials (created with Django admin)
    - Google login
3. Afer login, your email should appear in the navigation bar.

### Permission Testing
1. Not logged in:  
    - Attempt to access `/records/<int:pk>/update` or `/records/<int:pk>/delete`.
    - You should be redirected to login.
2. Logged in as a non-staff user who is NOT the owner:  
    - Attempt to access update/delete views for a patient you don't own.
    - You should see a 403 Forbidden error.
3. Logged in as the owner (non-staff):
    - You should be able to update or delete *your own* patient records.
3. Logged in as staff:  
    - You should be able to update or delete *any* patient records. 

## Example Git Commit
``` powershell
git add .
git commit -m 'feat: Add DRF API endpoints'
git push
```

## REST API Details

### Exposed Models

- Patient: Full CRUD support via API endpoints

### API URLs

- Base API endpoint:
```bash
/api/
```

- Patients endpoint:
```bash
/api/patients/
```

- API schema and documentation:
    - Swagger UI: `/api/schema/swagger-ui`
    - Redoc UI: `/api/schema/redoc/`

### Filtering, Searching, and Ordering

The API supports filtering, searching, and ordering via query parameters:

- Filtering by field:
    Use `?field=value` to filter records by exact field match.
    Example:
    ```bash
    /api/patients/?first_name=Walter
    ```

- Searching:
    Use `?search=term` to search across predefined fields.
    Example:
    ```bash
    /api/patients/?search=White
    ```

- Ordering:
    Use `?ordering=field` to order ascending or `?ordering=-field` for descending order.
    Example:
    ```bash
    /api/patients/?ordering=date_of_birth
    ```

You can combine these parameters as needed:
```bash
/api/patients/?last_name=Potter&ordering=date_of_birth
```

### Pagination

- The API uses pagination to limit the number of results per response.
- Defualt page size: 10 patients per page.
- Use the `?page=` query parameter to navigate pages.
Example:
```bash
/api/patients/?page2
```

### Custom Permission Logic

- Only owners of a patient record can update or delete it.
- Staff users have full access to update/delete any patient record.
- Unauthenticated users cannot update or delete patient records.
- Read (GET) operations are only accessible to authenticated users. 

### Testing the API

1. Start the server:
``` powershell
python manage.py runserver
```

2. Log in to the web frontend at:
``` bash
http://127.0.0.1.8000/accounts/login
```

3. Access the API browser interface:
```bash
http://127.0.0.1:8000/api/
```

4. Manually test permissions:  
    **Logged in as a regular user**  
        - Can view the patients list and individual patient records  
        - Can edit/delete only the patient records you created.  
    **Logged in as a staff user**  
        - Full access  
        - Can view, create, update, and delete any patient  
    **Not logged in**  
        - Cannot access the API at all  

## Docker Setup

### Environment Variables

- Copy `env.example` to `.env` and update your environment variables. 

### Build and Run the Application with Docker Compose

1. Build the Docker images:
```powershell
docker compose build
```

2. Start the containers in detached mode:
```powershell
docker compose up -d
```

3. Apply database migrations inside the web container
```powershell
docker compose exec web python manage.py migrate
```

4. Collect static files to serve CSS files:
```powershell
docker compose exec web python manage.py collectstatic --noinput
```

5. (Optional) Create a superuser inside the container:
```powershell
docker compose exec web python manage.py createsuperuser
```

### Accessing the Application

- Visit `http://localhost:8000` to use the web frontend.
- API base URL: `http://localhost:8000/api/`