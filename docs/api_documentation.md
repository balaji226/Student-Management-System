# REST API Documentation: Student Management System

The Student Management System exposes a full suite of RESTful API endpoints adhering to HTTP standards, standard JSON serialization, and status code conventions.

**Base URL**: `http://127.0.0.1:8000/api/`  
**Content-Type**: `application/json`

---

## Endpoint Summary Table

| Method | Endpoint | Description | Expected Status Codes |
|---|---|---|:---:|
| `POST` | `/api/students/` | Create a new student record | `201 Created`, `400 Bad Request` |
| `GET` | `/api/students/` | List all students (supports search & filters) | `200 OK` |
| `GET` | `/api/students/{id}/` | Retrieve a specific student by primary key | `200 OK`, `404 Not Found` |
| `PUT` | `/api/students/{id}/` | Fully update an existing student record | `200 OK`, `400 Bad Request`, `404 Not Found` |
| `PATCH` | `/api/students/{id}/` | Partially update student fields | `200 OK`, `400 Bad Request`, `404 Not Found` |
| `DELETE` | `/api/students/{id}/` | Permanently delete student record | `204 No Content`, `404 Not Found` |
| `GET` | `/api/students/stats/` | Retrieve summary metrics for dashboard | `200 OK` |

---

## 1. Create Student

- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
```json
{
  "register_number": "25AD3018",
  "name": "Balaji",
  "email": "balaji@example.com",
  "phone": "9876543210",
  "date_of_birth": "2005-05-14",
  "gender": "Male",
  "department": "AI&DS",
  "year": "I",
  "section": "A",
  "address": "124 Tech Park Avenue, Chennai",
  "admission_date": "2025-08-01",
  "status": "Active"
}
```
- **Success Response (`201 Created`)**:
```json
{
  "id": 1,
  "register_number": "25AD3018",
  "name": "Balaji",
  "email": "balaji@example.com",
  "phone": "9876543210",
  "date_of_birth": "2005-05-14",
  "gender": "Male",
  "department": "AI&DS",
  "year": "I",
  "section": "A",
  "address": "124 Tech Park Avenue, Chennai",
  "admission_date": "2025-08-01",
  "status": "Active",
  "created_at": "2026-09-17T13:40:00.123456Z",
  "updated_at": "2026-09-17T13:40:00.123456Z"
}
```
- **Error Response (`400 Bad Request` - Duplicate Register Number)**:
```json
{
  "register_number": [
    "Student with register number '25AD3018' already exists."
  ]
}
```

---

## 2. List All Students (with Search & Filters)

- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Optional Query Parameters**:
  - `?search=Balaji` (searches across name, register_number, and email)
  - `?department=AI&DS` (filters by specific department)
  - `?year=I` (filters by year of study)
  - `?status=Active` (filters by Active or Inactive)
  - `?page=1` (pagination page number)
- **Success Response (`200 OK`)**:
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "register_number": "25AD3018",
      "name": "Balaji R",
      "email": "balaji@example.com",
      "phone": "9876543210",
      "date_of_birth": "2005-05-14",
      "gender": "Male",
      "department": "AI&DS",
      "year": "I",
      "section": "A",
      "address": "124 Tech Park Avenue, Anna Nagar, Chennai",
      "admission_date": "2025-08-01",
      "status": "Active",
      "created_at": "2026-09-17T13:40:00Z",
      "updated_at": "2026-09-17T13:40:00Z"
    }
  ]
}
```

---

## 3. Retrieve Single Student by ID

- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Success Response (`200 OK`)**:
```json
{
  "id": 1,
  "register_number": "25AD3018",
  "name": "Balaji R",
  "email": "balaji@example.com",
  "phone": "9876543210",
  "date_of_birth": "2005-05-14",
  "gender": "Male",
  "department": "AI&DS",
  "year": "I",
  "section": "A",
  "address": "124 Tech Park Avenue, Anna Nagar, Chennai",
  "admission_date": "2025-08-01",
  "status": "Active",
  "created_at": "2026-09-17T13:40:00Z",
  "updated_at": "2026-09-17T13:40:00Z"
}
```
- **Error Response (`404 Not Found`)**:
```json
{
  "detail": "No Student matches the given query."
}
```

---

## 4. Full Update Student (PUT)

- **Method**: `PUT`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
```json
{
  "register_number": "25AD3018",
  "name": "Balaji Ramanathan",
  "email": "balaji.updated@example.com",
  "phone": "9998887776",
  "date_of_birth": "2005-05-14",
  "gender": "Male",
  "department": "AI&DS",
  "year": "II",
  "section": "B",
  "address": "New Residency, Chennai",
  "admission_date": "2025-08-01",
  "status": "Active"
}
```
- **Success Response (`200 OK`)**: Returns updated student object.

---

## 5. Partial Update Student (PATCH)

- **Method**: `PATCH`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Headers**: `Content-Type: application/json`
- **Request Body**:
```json
{
  "status": "Inactive"
}
```
- **Success Response (`200 OK`)**:
```json
{
  "id": 1,
  "register_number": "25AD3018",
  "name": "Balaji Ramanathan",
  "email": "balaji.updated@example.com",
  "status": "Inactive",
  ...
}
```

---

## 6. Delete Student

- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Success Response (`204 No Content`)**: Empty response body.
- **Error Response (`404 Not Found`)**:
```json
{
  "detail": "No Student matches the given query."
}
```

---

## 7. Dashboard Metrics API

- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/stats/`
- **Success Response (`200 OK`)**:
```json
{
  "total_students": 10,
  "active_students": 9,
  "inactive_students": 1,
  "departments_count": 6,
  "department_breakdown": [
    { "department": "AI&DS", "count": 2 },
    { "department": "CSE", "count": 2 },
    { "department": "ECE", "count": 2 },
    { "department": "IT", "count": 1 },
    { "department": "EEE", "count": 1 },
    { "department": "MECH", "count": 1 },
    { "department": "CIVIL", "count": 1 }
  ]
}
```
