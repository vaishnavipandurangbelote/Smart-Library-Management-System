# 📚 Smart Library Management System

<p align="center">
  <strong>📖 Simplifying Library Management Through Technology</strong>
  <br>
  A Full-Stack Web Application Powered by Flask REST API and SQLite
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-REST%20API-black?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white" alt="SQLite">
</p>

---

## 🌟 About the Project

**Smart Library Management System** is a web-based application designed to simplify and organize library operations through a clean user interface and a Flask-powered RESTful API.

The application provides essential book management functionality, allowing users to add, view, update, and delete book records while maintaining information in an SQLite database.

It demonstrates the integration of frontend technologies, backend development, REST API communication, and database management in a real-world application.

## ✨ Key Features

- 📖 **Book Management** – Add and maintain book records.
- 📚 **View Books** – Retrieve and display available library records.
- 🔄 **Issue & Return Management** – Update book availability status.
- 🗑️ **Delete Records** – Remove unwanted book entries.
- 🔗 **RESTful API** – Handle application requests through HTTP methods.
- 💾 **Database Integration** – Store book information using SQLite.
- 🎨 **User-Friendly Interface** – Simple and organized web interface.
- ⚡ **Dynamic Updates** – Communicate with the backend using JavaScript Fetch API.

## 🛠️ Technology Stack

| Technology | Application                    |
| ---------- | ------------------------------ |
| Python     | Backend Programming            |
| Flask      | RESTful API Development        |
| HTML5      | Frontend Structure             |
| CSS3       | Styling and Layout             |
| JavaScript | Frontend-Backend Communication |
| SQLite     | Database Management            |

## 🏗️ System Architecture

The application follows a simple three-layer architecture:

```text
        👤 USER
           |
           ▼
   ┌──────────────────┐
   │     FRONTEND     │
   │   HTML / CSS     │
   │    JavaScript    │
   └──────────────────┘
           |
           ▼
   ┌──────────────────┐
   │      BACKEND     │
   │   Python Flask   │
   │    RESTful API   │
   └──────────────────┘
           |
           ▼
   ┌──────────────────┐
   │     DATABASE     │
   │      SQLite      │
   │     library.db   │
   └──────────────────┘
```

## 🔗 REST API Endpoints

| HTTP Method | Endpoint      | Description        |
| ----------- | ------------- | ------------------ |
| GET         | `/books`      | Retrieve all books |
| POST        | `/books`      | Add a new book     |
| PUT         | `/books/<id>` | Update book status |
| DELETE      | `/books/<id>` | Delete a book      |

### 📡 API Communication

The frontend communicates with the Flask backend using JavaScript Fetch API.

- GET requests retrieve book records.
- POST requests submit new book information.
- PUT requests update existing book details.
- DELETE requests remove book records.

API responses are exchanged in JSON format.

## 📂 Project Structure

```text
SmartLibraryAPI/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .gitignore
```

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vaishnavipandurangbelote/Smart-Library-Management-System.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Smart-Library-Management-System
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5️⃣ Install Flask

```bash
pip install flask
```

### 6️⃣ Run the Application

```bash
python app.py
```

### 7️⃣ Open the Application

```text
http://127.0.0.1:5000
```

## 🧪 Experimental Testing

| Test Case             | Expected Result                   |
| --------------------- | --------------------------------- |
| Add a book            | New book record is created        |
| Retrieve books        | Stored book records are displayed |
| Update book status    | Book status is modified           |
| Delete a book         | Selected record is removed        |
| Database verification | Changes are reflected in SQLite   |

## 🎯 Project Objectives

- Understand RESTful API development using Flask.
- Implement CRUD operations using HTTP methods.
- Integrate frontend technologies with a Python backend.
- Perform database operations using SQLite.
- Explore API request and response handling using JSON.
- Experimentally test REST API functionality.

## 🚀 Future Enhancements

- 🔐 User authentication and role-based access.
- 🔍 Advanced book search and filtering.
- 👥 Member registration and management.
- 📅 Book borrowing and return date tracking.
- 📊 Library analytics and dashboard.
- 📋 Borrowing history and reports.

## 👩‍💻 Developer

**Vaishnavi Pandurang Belote**

Developed as a Full-Stack Flask REST API project using Python, Flask, HTML, CSS, JavaScript, and SQLite.

---

<p align="center">
  <strong>💻 Designed & Developed by Vaishnavi Pandurang Belote</strong>
  <br>
  <sub>Smart Library Management System | Flask REST API Project</sub>
  <br><br>
  ⭐ If you find this project interesting, consider giving it a star!
</p>
