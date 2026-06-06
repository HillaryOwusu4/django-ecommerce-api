# Django E-Commerce REST API

A production-ready REST API for an e-commerce platform built with Django and Django REST Framework.

## Features
- Full Products CRUD API
- Orders API with nested product details
- JWT Authentication (login, protected endpoints)
- Django Admin panel

## Tech Stack
- Python 3.11
- Django 6.0
- Django REST Framework
- SimpleJWT
- SQLite (dev) / PostgreSQL (prod)

## Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | /api/products/ | List & create products |
| GET/PUT/DELETE | /api/products/:id/ | Single product |
| GET/POST | /api/orders/ | List & create orders |
| POST | /api/token/ | Login — get JWT tokens |
| POST | /api/token/refresh/ | Refresh access token |

## Setup
```bash
git clone https://github.com/HillaryOwusu4/django-ecommerce-api
cd django-ecommerce-api
python -m venv venv
source venv/Scripts/activate
pip install django djangorestframework djangorestframework-simplejwt Pillow
python manage.py migrate
python manage.py runserver
```

