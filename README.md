### **README.md**

# **Patient Management System**

This is a Django-based RESTful API for managing patient information, including their family members, medications, and demographics.

---

## **Prerequisites**

Ensure the following tools are installed on your system:

1. **Python** (3.8+ recommended)
2. **pip** (Python package manager)
3. **virtualenv** (for creating isolated Python environments)
4. **Git**

---

## **Setup Instructions**

### 1. **Clone the Repository**

First, clone the project repository:

```bash
git clone <repository-url>
cd <project-folder>
```

---

### 2. **Create and Activate Virtual Environment**

Create a virtual environment for the project:

```bash
python -m venv venv
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 3. **Install Dependencies**

Install all the required Python packages:

```bash
pip install -r requirements.txt
```

---


### 4. **Apply Migrations**

Run the following commands to create database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. **Create Superuser (Optional)**

To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

---

### 6. **Start the Development Server**

Run the following command to start the Django server on **port 8000** (default):

```bash
python manage.py runserver
```

To use a custom port, add it at the end, e.g., port 8080 or 8001:

```bash
python manage.py runserver 8080
```

---

### 8. **Access the Application**

- **Swagger UI** (API Documentation):Visit: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)
- **Redoc UI**:Visit: [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)
- **Admin Panel**:
  Visit: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

By following the steps above, you should be able to set up and run the application on any system. 🚀

## Additional details:

## **Project Structure**

```
project-root/
│-- manage.py
│-- patient_management/       # Django project settings
│   └── settings.py
│-- core/                     # Main app for patient management
│   ├── models.py             # Database models
│   ├── views.py              # API views
│   ├── serializers.py        # DRF serializers
│   └── urls.py               # App-specific URLs
│-- templates/                # HTML templates (if needed)
│-- static/                   # Static files (CSS, JS)
│-- .gitignore
│-- requirements.txt          # Project dependencies
│-- README.md                 # Project documentation
```

---

## **API Endpoints**

| Endpoint                               | Method   | Description                 |
| -------------------------------------- | -------- | --------------------------- |
| `/api/patients/`                     | `GET`  | List all patients           |
| `/api/patients/`                     | `POST` | Create a new patient        |
| `/api/patients/{id}/`                | `GET`  | Retrieve a specific patient |
| `/api/patients/{id}/`                | `PUT`  | Update a specific patient   |
| `/api/patients/{id}/family-members/` | `POST` | Add a family member         |
| `/api/patients/{id}/medications/`    | `POST` | Add a medication            |

---
