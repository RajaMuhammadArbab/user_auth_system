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

## Project Demo

<img width="1395" height="782" alt="1" src="https://github.com/user-attachments/assets/02c0b881-6cb5-4fe8-8bf9-7aeceb544a41" />
<img width="1401" height="714" alt="2" src="https://github.com/user-attachments/assets/bb1613fb-e49e-48b8-9bc4-9e3e118ea954" />
<img width="1404" height="674" alt="Captur3" src="https://github.com/user-attachments/assets/54cda932-6c3c-413f-ad78-6d35ce7677db" />
<img width="1380" height="853" alt="4" src="https://github.com/user-attachments/assets/34605d5a-2b00-4d9e-a9a5-25a0ae14950c" />
<img width="1369" height="896" alt="5" src="https://github.com/user-attachments/assets/48c076c2-e1ce-441a-9421-8e7e77c61905" />
<img width="1405" height="446" alt="6" src="https://github.com/user-attachments/assets/a2a1d36d-643a-48e7-9acc-0fc95918e136" />
    
