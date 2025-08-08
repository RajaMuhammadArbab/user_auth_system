# Django Role-Based Access Control API

This project is a Django REST Framework (DRF) API with role-based permissions for Admin, Editor, and Viewer roles.

##  Features
- JWT Authentication
- Role-based access control
- Admin-only endpoints
- Owner profile editing
- PostgreSQL database support

##  Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate 
venv\Scripts\activate   
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database
Edit `settings.py` to match your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'auth_db',
        'USER': 'postgres',
        'PASSWORD': 'arbab786',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create a superuser
```bash
python manage.py createsuperuser
```

### 7️⃣ Run the server
```bash
python manage.py runserver
```

### 8️⃣ API Authentication
Obtain JWT token:
```http
POST /api/token/
{
    "username": "rajamuhammadarbab",
    "password": "arbab786"
}
```

Use the token for authenticated requests:
```
Authorization: Bearer your_token_here
```

## 🛠 Testing in Django Shell
```bash
python manage.py shell
>>> from django.contrib.auth import get_user_model
>>> User = get_user_model()
>>> u = User.objects.get(username="rajamuhammadarbab")
>>> (u.role, u.is_staff, u.is_superuser)
```

---

