# StellarCare

This is a Django-based Hospital Management System that implements CRUD operations for patient records. The system allows users to create, read, update, and delete patient information. Authentication and permissions are implemented to protect sensitive operations.


## Base URL Path

The base URL path for accessing the app's view is:
```bash
/records/
```

## CRUD Operations

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
    - Attempt to access /records/<pk>/update or /records/<pk>/delete
    - You should be redirected to login.
2. Logged in as non-staff:  
    - Access update/delete views.
    - You should see a 403 Forbidden error.
3. Logged in as staff:  
    - You should be able to update or delete patient records. 