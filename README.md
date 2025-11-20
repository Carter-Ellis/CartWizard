🛒 CartWizard 🧙‍♂️
AI-Powered Supermarket Web Application (Python, Django, PostgreSQL)

🚀 CartWizard is a full-stack supermarket web application built with Python, Django, and PostgreSQL. It allows users to browse products, add items to their cart, and later will include an AI-powered cart summary using an LLM API.
This project is being built as a hands-on way to practice full-stack web development, database modeling, Python OOP, and eventually AI integration.

---------------------------------------
🧠 Features (Planned and In Progress)

- AI-powered cart summary using an LLM API
- Product browsing and categories
- Shopping cart with item quantities
- User authentication (login, signup, logout)
- Clean Django template frontend

---------------------------------------
🛠️ Tech Stack

Frontend:
- HTML (Django Templates)
- CSS (Tailwind planned)
- Optional small JavaScript

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

---------------------------------------
📌 Project Status

This project is currently in the early development phase.
The base Django setup, PostgreSQL configuration, and initial app structure are complete.
Models, views, templates, and the AI feature will be implemented next.

---------------------------------------
📄 License

This project is intended for educational and portfolio use.
