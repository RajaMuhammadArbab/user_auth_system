# Sample Test User Credentials for Review API

Use these accounts to test the Review API.

---

## 1. Admin User
**Username:** `adminuser`  
**Password:** `AdminPass123!`  
**Role:** `admin`  

Has full access to all endpoints (can create, update, delete any review).

**Create via command:**
```bash
python manage.py createsuperuser --username adminuser --email admin@example.com
```
Set password to `AdminPass123!` when prompted.

---

## 2. Regular User
**Username:** `testuser`  
**Password:** `UserPass123!`  
**Role:** `user`  

Can only create and view their own reviews.

**Create via Django shell:**
```bash
python manage.py shell
```
```python
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_user(username="testuser", password="UserPass123!", role="user")
```
