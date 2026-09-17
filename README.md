# Student Management System (SMS)

A complete, professional, beginner-friendly full-stack web application designed for academic institutions to manage student records via a modern responsive interface and Django REST Framework APIs.

![Student Management System](static/images/logo.svg)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Problem Statement & Objectives](#problem-statement--objectives)
3. [Key Features](#key-features)
4. [Technology Stack](#technology-stack)
5. [System Architecture](#system-architecture)
6. [Project Structure](#project-structure)
7. [Database Schema & Design](#database-schema--design)
8. [REST API Documentation](#rest-api-documentation)
9. [Validation Rules](#validation-rules)
10. [Automated & Manual Testing](#automated--manual-testing)
11. [Installation & Setup Guide](#installation--setup-guide)
12. [Default Credentials](#default-credentials)
13. [How to Use the Application](#how-to-use-the-application)
14. [Git & GitHub Submission Guide](#git--github-submission-guide)
15. [Documentation Directory](#documentation-directory)
16. [Future Enhancements](#future-enhancements)

---

## 1. Project Overview
The **Student Management System** is a full-stack CRUD application allowing college administrators to seamlessly record, monitor, update, search, and delete student data. It combines a clean, modern, responsive frontend with a robust Python/Django backend and SQLite database.

---

## 2. Problem Statement & Objectives
- **Problem**: Traditional spreadsheets and paper files result in duplicate records, validation errors, and slow information retrieval during university examinations and audits.
- **Objectives**:
  - Centralize student records in a relational database.
  - Implement full CRUD operations with client-side and server-side validation.
  - Provide an executive dashboard with dynamic department statistics.
  - Support instant live search (by name, register number, email) and multi-factor filtering (department, study year, status).
  - Provide standardized RESTful APIs for third-party integrations and automated testing.

---

## 3. Key Features

### Modern Dashboard
- **Metric Cards**: Total Students, Active Students, Inactive Students, and Department count.
- **Department Distribution**: Progress bars showing department enrollment percentages.
- **Recent Admissions Table**: Quick glance at newly enrolled students.
- **Quick Actions**: 1-click links to add a student or filter the directory.

### Complete Student CRUD
- **Create**: Comprehensive registration form with immediate client and server validations.
- **Read**: Clean, responsive table with status badges (`Active` / `Inactive`), department pills, and pagination.
- **Update**: Pre-populates all student attributes with validation before saving.
- **Delete**: Safety confirmation modal dialog to avoid accidental deletion.
- **Detail View**: Student ID Card profile card with print-friendly layout.

### Dynamic Search and Filtering
- Search across **Name**, **Register Number**, and **Email** simultaneously with automatic debouncing.
- Filter dropdowns for **Department**, **Year of Study**, and **Enrollment Status**.
- Quick "Clear Filters" button.

### RESTful API
- Standard endpoints (`POST`, `GET`, `PUT`, `PATCH`, `DELETE`) with JSON serialization and HTTP status codes.
- `/api/students/stats/` endpoint powering dynamic client widgets.

### Administrator Authentication
- Secure Django session-based login and logout.
- 1-click **Auto Fill Demo Credentials** button on the login screen for rapid evaluation.

---

## 4. Technology Stack
- **Frontend**: HTML5, CSS3 (Modern Vanilla CSS with Glassmorphism, CSS Variables, and Flex/Grid), Vanilla JavaScript (ES6+).
- **Backend**: Python 3.14, Django 6.1, Django REST Framework 3.18, django-cors-headers.
- **Database**: SQLite 3 (`db.sqlite3`).
- **Testing**: Django `TestCase` / `APITestCase`, Postman.
- **Version Control**: Git & GitHub.

---

## 5. System Architecture
```
+-------------------------------------------------------------------------+
|                              CLIENT BROWSER                             |
|  - HTML5 Responsive Views (Inter Typography, Glassmorphism Cards)       |
|  - Vanilla JavaScript (Regex Validation, Debounced Search, Modals)      |
+------------------------------------+------------------------------------+
                                     | HTTP Requests (Form / JSON)
                                     v
+-------------------------------------------------------------------------+
|                              DJANGO BACKEND                             |
|  - URL Router & Django Authentication Middleware                        |
|  - Template Views & DRF ModelViewSet                                    |
|  - Serializer with Unique & Regex Validation Rules                      |
+------------------------------------+------------------------------------+
                                     | Django ORM
                                     v
+-------------------------------------------------------------------------+
|                            SQLITE 3 DATABASE                            |
|  - students_student table with Unique Indexes & Field Constraints       |
+-------------------------------------------------------------------------+
```

---

## 6. Project Structure
```
student_management_system/
│
├── manage.py                  # Django administrative script
├── requirements.txt           # Project dependencies
├── README.md                  # Complete project documentation
├── .gitignore                 # Git ignore configuration
├── db.sqlite3                 # SQLite database file
│
├── config/                    # Project configuration package
│   ├── __init__.py
│   ├── settings.py            # App settings, DB, static files, DRF
│   ├── urls.py                # Root routing
│   ├── asgi.py
│   └── wsgi.py
│
├── students/                  # Core student management app
│   ├── migrations/            # Database migration scripts
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py   # Populates admin & 10 sample students
│   ├── __init__.py
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Student model definition
│   ├── serializers.py         # DRF Serializers with field validators
│   ├── urls.py                # Student views & API router
│   ├── views.py               # Frontend views and REST ViewSet
│   └── tests.py               # Automated test suite (14 test cases)
│
├── templates/                 # Frontend HTML templates
│   ├── base.html              # Core layout with sidebar and navbar
│   ├── login.html             # Login card with 1-click demo fill
│   ├── dashboard.html         # Overview dashboard & metrics
│   ├── students.html          # Student directory, filters, table
│   ├── add_student.html       # Add student form
│   ├── edit_student.html      # Edit student form
│   └── student_detail.html    # Student ID Card & printable summary
│
├── static/                    # Static assets
│   ├── css/
│   │   └── style.css          # Design system & responsive styles
│   ├── js/
│   │   └── script.js          # Client-side validation & modal logic
│   └── images/
│       └── logo.svg           # High-resolution vector logo
│
└── docs/                      # Comprehensive technical documentation
    ├── project_overview.md    # Problem statement, objectives, architecture
    ├── database_design.md     # ER diagram, table schemas, data dictionary
    ├── api_documentation.md   # Complete REST API specifications
    ├── testing.md             # Automated test logs & Postman guide
    └── viva_questions.md      # 25 Q&A for viva voce preparation
```

---

## 7. Database Schema & Design
The `Student` model contains the following fields:
- `id` (AutoField, Primary Key)
- `register_number` (CharField 20, Unique, Indexed)
- `name` (CharField 100)
- `email` (EmailField 100, Unique)
- `phone` (CharField 15, 10-digit validation)
- `date_of_birth` (DateField, past date check)
- `gender` (`Male`, `Female`, `Other`)
- `department` (`AI&DS`, `CSE`, `IT`, `ECE`, `EEE`, `MECH`, `CIVIL`)
- `year` (`I`, `II`, `III`, `IV`)
- `section` (`A`, `B`, `C`)
- `address` (TextField, optional)
- `admission_date` (DateField)
- `status` (`Active`, `Inactive`)
- `created_at` & `updated_at` (Audit timestamps)

---

## 8. REST API Documentation

| Method | Endpoint | Description | Status Code |
|---|---|---|:---:|
| `POST` | `/api/students/` | Create student | `201 Created` |
| `GET` | `/api/students/` | List all students (supports search & filters) | `200 OK` |
| `GET` | `/api/students/{id}/` | Retrieve single student by ID | `200 OK` |
| `PUT` | `/api/students/{id}/` | Full update | `200 OK` |
| `PATCH` | `/api/students/{id}/` | Partial update | `200 OK` |
| `DELETE` | `/api/students/{id}/` | Delete student | `204 No Content` |
| `GET` | `/api/students/stats/` | Dashboard metrics | `200 OK` |

*Refer to [docs/api_documentation.md](docs/api_documentation.md) for full request/response samples.*

---

## 9. Validation Rules
- **Register Number**: Minimum 3 characters, uppercase, unique across database.
- **Full Name**: Minimum 2 characters.
- **Email**: Standard RFC format, unique across database.
- **Phone Number**: Exactly 10 to 15 numeric digits.
- **Date of Birth**: Must be in the past (`< today`).
- **All Required Fields**: Enforced by HTML5, JavaScript listeners, and Django DRF serializers.

---

## 10. Automated & Manual Testing

### Running Django Automated Tests
```bash
python manage.py test students
```
**Result**: 14 tests run in 0.11s with 100% pass rate (`OK`).

### Postman Testing
Sample payloads and test assertions for all endpoints are documented in [docs/testing.md](docs/testing.md).

---

## 11. Installation & Setup Guide

### Step 1: Clone or Navigate to Project Directory
```bash
cd student_management_system
```

### Step 2: Create and Activate Virtual Environment (Optional but Recommended)
**Windows (PowerShell/CMD)**:
```powershell
python -m venv venv
venv\Scripts\activate
```
**Linux / macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Seed Sample Data & Admin Superuser
Run the included seed command to automatically create the administrator account and 10 sample students:
```bash
python manage.py seed_data
```

*(Alternatively, you can manually run `python manage.py createsuperuser`)*

### Step 6: Start the Development Server
```bash
python manage.py runserver
```
Access the application at: **`http://127.0.0.1:8000/`**

---

## 12. Default Credentials
For quick evaluation, use the pre-configured admin account:
- **Username**: `admin`
- **Password**: `admin123`
*(A "Auto Fill" button is also available directly on the login page).*

---

## 13. How to Use the Application
1. Open `http://127.0.0.1:8000/login/` in your browser.
2. Click **Auto Fill** and then **Sign In to Dashboard**.
3. Inspect key metrics and department distribution bars on the **Dashboard**.
4. Click **Students Directory** to view the student table.
5. Try the live search box (type "Balaji" or "25CS") or select a department filter.
6. Click **Add Student** to enroll a new student. Test validation by leaving a field blank or providing an invalid phone number.
7. Click the **View (Eye)** icon on any student row to view the institutional ID profile card.
8. Click **Edit (Pencil)** to update information.
9. Click **Delete (Trash)** to open the confirmation modal dialog.
10. Explore Django Admin at `http://127.0.0.1:8000/admin/` or the REST API at `http://127.0.0.1:8000/api/students/`.

---

## 14. Git & GitHub Submission Guide

### Initializing Git and Creating Commits
If you are submitting this repository to GitHub, follow these standard steps:

```bash
# 1. Initialize git repository
git init

# 2. Stage all project files (.gitignore will exclude venv and cache)
git add .

# 3. Create structured milestone commits
git commit -m "Initial project setup with Django, DRF, and project architecture"
git commit -m "Create Student model with unique constraints and validations"
git commit -m "Implement DRF serializers and REST API endpoints"
git commit -m "Implement student CRUD template views and authentication"
git commit -m "Add responsive frontend UI with dashboard metrics and search/filter"
git commit -m "Add automated unit tests and seed data command"
git commit -m "Add comprehensive college documentation and viva questions"

# 4. Link to your GitHub repository
git remote add origin https://github.com/<your-username>/student-management-system.git
git branch -M main
git push -u origin main
```

---

## 15. Documentation Directory
Detailed technical artifacts are available in the `docs/` folder:
- [docs/project_overview.md](docs/project_overview.md) — Problem statement, architecture, features.
- [docs/database_design.md](docs/database_design.md) — ER diagram (Mermaid) and data dictionary.
- [docs/api_documentation.md](docs/api_documentation.md) — Complete endpoint specs and payloads.
- [docs/testing.md](docs/testing.md) — Test logs and 10 Postman test cases.
- [docs/viva_questions.md](docs/viva_questions.md) — 25 first-year beginner viva Q&A.

---

## 16. Future Enhancements
- Dedicated student and teacher login portals.
- Semester-wise attendance and GPA grade card tracking.
- Online fees payment integration.
- SMS and WhatsApp automated alert notifications for parents.
- Export student records to PDF and Excel formats.
