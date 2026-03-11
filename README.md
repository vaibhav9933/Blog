# 📝 Django Blog Website

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-5.2-green)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![Status](https://img.shields.io/badge/Status-Live-success)

A **full-featured Blog Management System** built using the **Django Web Framework** with role-based access control, blog post management, and commenting functionality.

🌐 **Live Website**  
https://vaibhav333.pythonanywhere.com/

---

# 📌 Project Overview

This project was developed during my **Web Development Internship** as part of practical training in **Django web application development**.

The system allows administrators, editors, and managers to efficiently manage blog content while users can browse articles and interact with posts.

The project demonstrates real-world implementation of:

- Django MVC architecture
- Role-based authentication
- CRUD operations
- Media file uploads
- Responsive UI design
- Commenting system

---

# 🏢 Internship Details

| Field | Information |
|------|-------------|
| Project Title | Django Blog Management System |
| Role | Web Development Intern |
| Technology | Python, Django, Bootstrap |
| Deployment | PythonAnywhere |
| Purpose | Build a dynamic blogging platform |

---

# ✨ Features

## 👤 Role-Based User System

| Role | Permissions |
|-----|-------------|
| **Admin (Project Head)** | Full system control |
| **Editors** | Create and edit blog posts |
| **Managers** | Manage users and posts |

---

## 📰 Blog Management

Users with permissions can:

- Create blog posts
- Edit posts
- Delete posts
- Add categories
- Upload images in blog posts

---

## 💬 Comment System

Visitors and users can:

- Comment on blog posts
- Interact with content
- Participate in discussions

---

## 📊 Admin Dashboard

The dashboard allows administrators to:

- Manage users
- Manage blog posts
- Manage categories
- Monitor platform activity

---

## 📱 Responsive Design

The website works smoothly on:

- Desktop
- Tablet
- Mobile devices

Implemented using **Bootstrap responsive design**.

---

# 📸 Project Screenshots

## Homepage


<img width="1920" height="1078" alt="Image" src="https://github.com/user-attachments/assets/e6f56b28-2d26-4aac-b02c-aafaa76d8a61" />


## Blog Post Page


<img width="1920" height="1078" alt="Image" src="https://github.com/user-attachments/assets/f5c4298b-f72e-4159-9687-1d8f63ed7447" />


## Dashboard

 
<img width="1920" height="1078" alt="Image" src="https://github.com/user-attachments/assets/b9c5e60f-2cbf-45ab-8214-d21153b93cdb" />



# 🏗 System Architecture

```
User (Browser)
      │
      ▼
Frontend (HTML, CSS, Bootstrap)
      │
      ▼
Django Views (Business Logic)
      │
      ▼
Django Models
      │
      ▼
SQLite Database
```

---

# 🗄 Database Schema (Simplified)

Main models used in the system:

```
User
 ├── id
 ├── username
 ├── password
 ├── role

Post
 ├── id
 ├── title
 ├── content
 ├── author
 ├── category
 ├── created_at

Category
 ├── id
 ├── name

Comment
 ├── id
 ├── post
 ├── user
 ├── text
 ├── created_at
```

---

# 🛠 Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| Bootstrap | Frontend styling |
| django-crispy-forms | Form rendering |
| Pillow | Image processing |

---

# ⚙️ Installation

## 1 Clone the repository

```bash
git clone https://github.com/your-username/blog-website.git
cd Blog
```

---

## 2 Create virtual environment

```bash
python -m venv env
```

Activate environment

### Windows

```bash
.\env\Scripts\Activate.ps1
```

### Linux / Mac

```bash
source env/bin/activate
```

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Apply migrations

```bash
python manage.py migrate
```

---

## 5 Create superuser

```bash
python manage.py createsuperuser
```

---

## 6 Run development server

```bash
python manage.py runserver
```

---

# 🚀 Usage

| Page | URL |
|-----|-----|
| Homepage | http://127.0.0.1:8000 |
| Admin Panel | http://127.0.0.1:8000/admin |
| Dashboard | http://127.0.0.1:8000/dashboard |

---

# 🌐 Deployment

This project is deployed on **PythonAnywhere**.

Deployment steps included:

- Configuring static files
- Configuring media files
- Running migrations
- Setting ALLOWED_HOSTS in Django settings

🔗 Live Website  
https://vaibhav333.pythonanywhere.com/

---

# 📂 Project Structure

```
Blog/
│
├── about_us/
├── blogs/
├── dashboards/
├── blog_main/
│
├── templates/
├── static/
├── media/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
└── README.md
```

---

# 🔮 Future Improvements

Planned enhancements:

- Blog search functionality
- Like & share system
- Rich text editor
- REST API (Django REST Framework)
- Pagination for blog posts
- Email notification system

---

# 👨‍💻 Author

Rahane Vaibhav Kailash  
B.Tech – Computer Science Engineering  
Parul University  

📧 2203051050601@paruluniversity.ac.in

---

# 📜 License

This project was developed as part of an **internship training program and academic learning**.
