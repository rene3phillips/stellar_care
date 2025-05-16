# StellarCare

This is a Django-based Hospital Management System that implements CRUD operations for patient records. The system allows users to create, read, update, and delete patient information.


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

### 4. Create a .env file 
Create a `.env` file based on `env.example` and fill in actual database credentials. 

### 5. Run Migrations
```powershell
python manage.py migrate
```

### 6. Create a superuser
```powershell
python manage.py createsuperuser
```
Follow the prompts to create a user account for the Django admin site.

### 7. Run the development server
```powershell
python manage.py runserver
```