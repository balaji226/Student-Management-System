# Viva Voce Preparation Guide: Student Management System

This guide contains **25 essential questions and clear, beginner-friendly answers** prepared specifically for engineering college viva examinations, project presentations, and lab evaluations.

---

### Q1: What is CRUD?
**Answer:**
CRUD stands for **Create, Read, Update, and Delete**. These are the four fundamental operations performed on persistent data in any database application:
- **Create**: Adding a new student record to the database.
- **Read**: Viewing or retrieving the list and details of students.
- **Update**: Modifying existing student data (e.g., updating phone number or year).
- **Delete**: Removing an unwanted student record from the system.

---

### Q2: What is Django?
**Answer:**
Django is a high-level, open-source **Python web framework** that encourages rapid development and clean, pragmatic design. It follows the **MVT (Model-View-Template)** architectural pattern and comes with built-in features such as an ORM, authentication system, admin dashboard, and CSRF protection.

---

### Q3: What is a REST API?
**Answer:**
REST stands for **Representational State Transfer**. A REST API is a web service architecture that allows different software applications (like a browser, mobile app, or frontend) to communicate with a backend server using standard HTTP requests (`GET`, `POST`, `PUT`, `DELETE`) and exchange structured data, most commonly in **JSON** format.

---

### Q4: What is HTTP?
**Answer:**
HTTP stands for **Hypertext Transfer Protocol**. It is the underlying communication protocol used by the World Wide Web. It establishes rules for how messages and data are formatted, transmitted, and handled between a web client (like Chrome) and a web server (like Django).

---

### Q5: What is the difference between GET and POST?
**Answer:**
- **GET**: Used to **request/retrieve data** from the server. Data parameters are sent in the URL query string (e.g., `?search=Balaji`). It does not modify data on the server and is safe to be bookmarked and cached.
- **POST**: Used to **send and create new data** on the server. Data is transmitted securely inside the HTTP request body rather than the URL. It is used for submitting forms, registering students, or logging in.

---

### Q6: What is the difference between PUT and PATCH?
**Answer:**
- **PUT**: Replaces the **entire resource**. All required fields must be supplied in the request; missing fields may be overwritten or cleared.
- **PATCH**: Performs a **partial update**. Only the specific fields that need to be changed are sent in the request (e.g., changing just `status: "Inactive"` while leaving all other fields intact).

---

### Q7: What is DELETE in HTTP?
**Answer:**
The `DELETE` HTTP method is used to instruct the server to permanently remove a specified resource identified by its unique URL (such as `DELETE /api/students/5/`). When successful, the server usually responds with an HTTP status code of `204 No Content`.

---

### Q8: What is SQLite?
**Answer:**
SQLite is a lightweight, self-contained, serverless relational database engine. Unlike traditional databases (like MySQL or PostgreSQL) that run as separate background services, SQLite stores the entire database in a single disk file (`db.sqlite3`). It is included with Python by default, making it ideal for development and college project demonstrations.

---

### Q9: What is an ORM (Object-Relational Mapping)?
**Answer:**
An ORM is a programming technique that allows developers to interact with relational databases using object-oriented code instead of writing raw SQL queries. In Django, instead of writing `SELECT * FROM students WHERE id=1;`, we write `Student.objects.get(id=1)`. The ORM automatically translates Python code into secure SQL statements.

---

### Q10: What is a Django Model?
**Answer:**
A Django Model is a Python class that inherits from `django.db.models.Model`. It defines the structure, fields, and constraints of a database table. Each attribute of the model class represents a database column (such as `name = models.CharField(max_length=100)`).

---

### Q11: What is a Serializer in Django REST Framework?
**Answer:**
A Serializer converts complex Django Model instances or querysets into native Python data types that can easily be rendered into **JSON**. Serializers also perform deserialization—converting incoming JSON request payloads back into validated Python objects before saving them to the database.

---

### Q12: What is JSON?
**Answer:**
JSON stands for **JavaScript Object Notation**. It is a lightweight, text-based, human-readable data format used universally for transmitting data between web servers and client applications using simple key-value pairs and arrays.

---

### Q13: What is Data Validation?
**Answer:**
Validation is the process of inspecting incoming data to verify that it satisfies expected types, formats, constraints, and business logic before it is processed or saved into the database (e.g., verifying that a phone number contains 10 numeric digits and that an email has an `@` symbol).

---

### Q14: What is a Primary Key?
**Answer:**
A Primary Key is a column (or combination of columns) in a relational database table that **uniquely identifies each record or row**. A primary key cannot contain `NULL` values, and no two rows can have the same primary key value. In our project, Django automatically creates an auto-incrementing integer `id` as the primary key.

---

### Q15: What is a Unique Constraint?
**Answer:**
A Unique Constraint is a database rule enforcing that all values in a specific column must be distinct across all rows. In our Student Management System, both `register_number` and `email` have unique constraints to prevent two students from being enrolled with the same registration number or email.

---

### Q16: Why is Server-Side Validation required even if Frontend Validation is present?
**Answer:**
Frontend validation improves user experience by giving immediate feedback in the browser. However, frontend validation can easily be bypassed (e.g., by disabling JavaScript, using curl, Postman, or developer tools). **Server-side validation is mandatory for security and data integrity** because the server is the ultimate gatekeeper of the database.

---

### Q17: What is CORS (Cross-Origin Resource Sharing)?
**Answer:**
CORS is a browser security mechanism that restricts a web page from making AJAX requests to a different domain, protocol, or port than the one that served the page. When building APIs used by external frontends, CORS headers (such as `django-cors-headers`) must be configured on the server to permit cross-origin access.

---

### Q18: What is Postman?
**Answer:**
Postman is a popular API development and testing tool that allows developers to compose, send, and inspect HTTP requests (`GET`, `POST`, `PUT`, `DELETE`) against backend APIs. It displays the response status code, headers, JSON body, and execution time without needing a graphical frontend.

---

### Q19: What is Git and GitHub?
**Answer:**
- **Git**: A distributed version control system running locally on the computer that records changes made to code files over time and allows branching, merging, and reverting.
- **GitHub**: A cloud-based hosting platform for Git repositories that enables sharing, collaboration, portfolio building, and team project management.

---

### Q20: Explain the complete project workflow from Browser to Database.
**Answer:**
1. **User Action**: The administrator fills out the "Add Student" form in the browser and clicks "Save Student Record".
2. **Client Validation**: JavaScript validates that fields are non-empty, the email format is correct, and the phone number is 10 digits.
3. **HTTP Request**: The form data is sent to the Django backend as an HTTP POST request.
4. **URL Routing & Middleware**: Django matches the URL in `urls.py`, verifies the admin session and CSRF token.
5. **View & Serializer**: The view passes the payload to `StudentSerializer` to validate field rules and unique constraints.
6. **ORM & Database**: The validated data is converted into an SQL `INSERT` query by the Django ORM and saved in the SQLite `students_student` table.
7. **Response & Feedback**: Django responds with an HTTP status and redirects the user with a green success toast alert.

---

### Q21: What are Django Migrations?
**Answer:**
Migrations are Django's way of propagating changes made to Python models (adding a field, changing a constraint) into the underlying database schema.
- `python manage.py makemigrations`: Inspects models and generates new migration files.
- `python manage.py migrate`: Applies pending migration scripts to update the database tables.

---

### Q22: What is the purpose of `.gitignore`?
**Answer:**
A `.gitignore` file tells Git which files and folders should not be tracked or committed to the repository. Examples include virtual environments (`venv/`), Python cache files (`__pycache__/`, `*.pyc`), environment secrets (`.env`), and temporary OS files (`.DS_Store`).

---

### Q23: What HTTP Status Codes are used in this project?
**Answer:**
- `200 OK`: Request succeeded (GET, PUT, PATCH).
- `201 Created`: New student record successfully created (POST).
- `204 No Content`: Student record successfully deleted (DELETE).
- `400 Bad Request`: Validation failure (duplicate registration number, invalid email).
- `404 Not Found`: Student with requested ID does not exist.

---

### Q24: What is the Django Admin Panel?
**Answer:**
The Django Admin is a ready-to-use, web-based management interface automatically generated by Django based on registered models. It allows superusers to perform CRUD operations, inspect database records, filter, search, and manage user permissions out-of-the-box.

---

### Q25: What future enhancements could be added to this Student Management System?
**Answer:**
1. **Student & Faculty Portals**: Role-based access for students to view their own grades and attendance.
2. **Fee & Attendance Tracking**: Modules to record daily attendance and semester tuition fee payments.
3. **Automated Notifications**: Email and SMS alerts for semester registration and fee deadlines.
4. **Export & Analytics**: Exporting student directories to Excel/CSV and advanced charts using Chart.js.
