🛒 CartWizard 🧙‍♂️
AI-Powered Supermarket Web Application (Python, Django, PostgreSQL)

🚀 CartWizard is a full-stack supermarket web application built with Python, Django, and PostgreSQL. Users can browse products, manage a shopping cart, and receive AI-generated recipe suggestions powered by the OpenAI API (GPT-4o-mini).
This project serves as a hands-on exploration of full-stack development, database modeling, Python OOP, and practical AI integration.

---------------------------------------
🧠 Features

- 🥘 AI-powered recipe suggestions using the OpenAI API
- 🛍️ Product browsing
- 🛒 Shopping cart with item quantities
- 🔐 User authentication (login, signup)

---------------------------------------
🛠️ Tech Stack

Frontend:
- HTML
- CSS

Backend:
- Python
- Django
- Django ORM

Database:
- PostgreSQL

Tools:
- VS Code
- Git & GitHub
- Python virtual environment (venv)

---------------------------------------

🔧 Setup Instructions

1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

2. Install Django
pip install django

3. Install PostgreSQL driver
pip install psycopg2-binary

4. Configure the PostgreSQL database in cartwizard/settings.py

ENGINE: django.db.backends.postgresql
NAME: cartwizarddb
USER: postgres
PASSWORD: your_password
HOST: localhost
PORT: 5432

5. Apply migrations
python manage.py migrate

6. Start the development server
python manage.py runserver
-----------------------------------------
🛒 Adding Products Through the Admin Panel

CartWizard currently manages products and inventory through Django’s built-in admin interface. This allows you to easily create, update, and delete products without needing a frontend form.

✔️ Steps to Add Items Using the Admin Panel

1. Create a superuser (admin account): 
  python manage.py createsuperuser

2. Start the development server:
  python manage.py runserver

3. Visit the admin dashboard - Open your browser and go to:
  http://localhost:8000/admin/

4. Log in using your superuser credentials.

5. In the admin panel, you’ll see sections for:
Product
Category
Inventory
CartItem
Cart

6. Click Product → Add Product to create new store items.
