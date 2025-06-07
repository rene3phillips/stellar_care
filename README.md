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

## AWS Deployment

### AWS Services Used

- ECR (Elastic Container Registry): Stores the Docker images for StellarCare
- EC2 (Elastic Compute Cloud): Hosts the application using Docker
- IAM Role: Manages permissions for pushing/pulling images and EC2 instance management

## Create IAM Role for EC2 to Access ECR

1. Navigate to IAM -> Roles -> Create role
2. Select AWS service, under Use case select EC2
3. Attach permissions: select `AmazonEC2ContainerRegistryReadOnly`
4. Name the role: `EC2InstanceRoleForECR`
5. Create role

## Create ECR Repository

Go to AWS Console -> ECR -> Create repository -> name it `my-django-app`

## Pushing Docker Image to ECR

1. Authenticate Docker to your ECR repository:
``` powershell
aws ecr get-login-password --region YOUR_REGION | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com
```

2. Build your Docker image locally:
``` powershell
docker compose build web
```

3. Tag the Docker image for ECR:
``` powershell
docker tag my-django-app:latest YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com/my-django-app:latest
```

4. Push the tagged image to ECR:
``` powershell
docker push YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com/my-django-app:latest
```

## EC2 Instance Setup to Run Your Docker Compose App

1. Launch an EC2 instance (Amazon Linux 2) and select the IAM role you created earlier.

2. SSH into the EC2 instance:
```powershell
ssh -i your-key.pem ec2-user@YOUR_EC2_PUBLIC_IP
```

3. Install Docker and Docker Compose on EC2:
``` powershell
sudo yum update -y
sudo yum install -y docker docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
newgrp docker
docker --version
docker compose version
```

4. Authenticate Docker on EC2 to pull from ECR:
``` powershell
aws ecr get-login-password --region YOUR_REGION | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com
```

5. Pull your Docker Image from ECR:
```powershell
docker pull YOUR_AWS_ACCOUNT_ID.dkr.ecr.YOUR_REGION.amazonaws.com/my-django-app:latest
```

6. Copy your `docker-compose.yml` and `.env` file to the EC2 instance:
```powershell
scp -i your-key-.pem docker-compose.yml ec2-user@YOUR_EC2_PUBLIC_IP:/home/ec2-user
scp -i your-key-.pem .env ec2-user@YOUR_EC2_PUBLIC_IP:/home/ec2-user
```

7. Update your `docker-compose.yml` on EC2 to use the ECR image:
```yaml
version: '3.8'
services:
    web:
    # Use the image from ECR instead of building locally
    image: <aws_account_id>.dkr.ecr.<region>[.amazonaws.com/](https://.amazonaws.com/)<your_repo_name>:latest 
    container_name: django_web
    # Command just starts Gunicorn; migrations run separately
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000
    # volumes: # REMOVE or comment out the local code mount
    #  - .:/app 
    ports:
        # Map host port 8000 to container port 8000 (Gunicorn)
        - "8000:8000" 
    env_file:
        - .env 
    depends_on:
        - db 

    db:
    image: postgres:16-alpine
    container_name: postgres_db
    volumes:
        - postgres_data:/var/lib/postgresql/data/ 
    env_file:
        - .env 
    # No ports needed here for web service access

volumes:
    postgres_data:
```

8. Make sure your `.env` on EC2 matches the `env.example` file. DEBUG should be set to True for production. 

9. Run Docker Compose on EC2 to start your app:
```powershell
docker compose up -d
```

10. Apply database migrations:
```powershell
docker compose exec web python manage.py migrate
```

11. Collect static files:
```
docker compose exec web python manage.py collectstatic --noinput
```

12. Your application should now be accessible via `http:YOUR_EC2_PUBLIC_IP:8000`

## Kubernetes Local Development Setup & Monitoring Guide

### 1. Local Kubernetes Environment Setup

Install Minikube (https://minikube.sigs.k8s.io/docs/start/)

```powershell
minikube start
```

### 2. Django Health Check Endpoint

Make sure your Django app has a health check endpoint

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
```

Add this to your URLs if not already present.

### 3. Creating Kubernetes Secrets

Create secrets from environment files 

```powershell
kubectl create secret generic app-secret --from-env-file=k8s-pg-secrets.env
kubectl create secret generic app-secret --from-env-file=k8s-app-secrets.env
```

Make sure your DATABASE_URL host in the env file matches your Kubernetes service name for your DB

## 4. Local Image Management for Minikube

Build images inside Minikube's Docker environment

```powershell
minikube -p minikube docker-env --shell powershell | Invoke-Expression

docker build --no-cache -t stellar_care-web:latest .
```

## 5. Applying Kubernetes Manifests

Apply all your manifests with: 
```powershell
kubectl apply -f k8s/postgres-pvc.yaml -f k8s/postgres-deployment.yaml -f k8s/postgres-service.yaml -f k8s/app-configmap.yaml -f k8s/app-deployment.yaml -f k8s/app-service.yaml
```

## 6. Intalling kube-prometheus-stack with Helm

Add repo and install Prometheus and Grafana stack:
```powershell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prom-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace --version 72.0.1
```

## 7. Accessing Your Application

```powershell
minikube service app-service --url
```

## 8. Accessing Grafana

Get Grafana admin password:
```bash
kubectl get secret --namespace monitoring prom-stack-grafana \
  -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Port-forward Grafana to local machine:
```bash
kubectl port-forward --namespace monitoring svc/prom-stack-grafana 3000:80
```

Login at `http://localhost:3000` with user `admin` and retrieved password.

## 9. Running Database Migrations

Run Django migrations inside the app pod:

```powershell
kubectl exec -it <app-pod-name> -- python manage.py migrate
```

Replace <app-pod-name> with your actual pod name (kubectl get pods).

## 10. Scaling and Rolling Updates

- Scale Deployment:

```powershell
kubectl scale deployment app-deployment --replicas=3
kubectl get pods
```

- Rolling Update:
    1. Edit `k8s/app-deployment.yaml`, update `image:` tag to a new one
    2. Apply changes:
    ```powershell
    kubectl apply -f k8s/app-deployment.yaml
    ```
    3. Check rollout status:
    ```powershell
    kubectl rollout status deployment/app-deployment
    kubectl get pods
    ```
    4. Rollback if necessary:
    ```powershell
    kubectl rollout undo deployment/app-deployment
    ```

## ⚠️ Important Cost Warning

If using managed Kubernetes services like Amazon EKS, Google GKE or Azure AKS, be aware that clusters, node pools, and cloud resources can incur significant charges. Always:

- Monitor your cloud usage.
- Delete resources when not in use.
- Use free tiers or local clusters (Minikube/Docker Desktop) for development to avoid unexpected costs. 
