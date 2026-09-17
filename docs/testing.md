# Testing Guide & Results: Student Management System

This document outlines both the automated test suite and manual/Postman testing procedures for the **Student Management System**.

---

## 1. Automated Django Tests

The application includes an extensive automated test suite covering models, constraints, and REST API endpoints in `students/tests.py`.

### How to Run Automated Tests
```bash
python manage.py test students -v 2
```

### Test Suite Summary
| Test Case Function | Description | Tested Endpoint/Behavior | Expected Result |
|---|---|---|---|
| `test_student_str` | Verifies `__str__` representation | Model method | Formatted string output |
| `test_student_defaults` | Checks default status (`Active`) | Model defaults | Default values set |
| `test_get_all_students` | Verifies listing student records | `GET /api/students/` | `200 OK`, JSON list |
| `test_get_student_detail` | Retrieves single student by ID | `GET /api/students/{id}/` | `200 OK`, matching fields |
| `test_create_student_success` | Creates a new valid record | `POST /api/students/` | `201 Created`, record in DB |
| `test_create_duplicate_register_number` | Rejects duplicate register number | `POST /api/students/` | `400 Bad Request` |
| `test_create_duplicate_email` | Rejects duplicate email address | `POST /api/students/` | `400 Bad Request` |
| `test_invalid_phone_number` | Rejects short/alphabetic phone | `POST /api/students/` | `400 Bad Request` |
| `test_update_student_put` | Performs complete update | `PUT /api/students/{id}/` | `200 OK`, DB refreshed |
| `test_partial_update_patch` | Modifies status field only | `PATCH /api/students/{id}/` | `200 OK`, status changed |
| `test_delete_student` | Deletes existing record | `DELETE /api/students/{id}/` | `204 No Content`, removed |
| `test_search_by_name` | Filters records by name query | `GET /api/students/?search=..` | `200 OK`, matched records |
| `test_filter_by_department` | Filters records by dept | `GET /api/students/?department=..` | `200 OK`, dept records |
| `test_stats_endpoint` | Returns dashboard statistics | `GET /api/students/stats/` | `200 OK`, counts correct |

### Test Output Verification
```
Ran 14 tests in 0.115s
OK
Destroying test database for alias 'default'...
```

---

## 2. Postman Testing Guide

### Prerequisites
1. Ensure the Django server is running locally:
   ```bash
   python manage.py runserver
   ```
2. Set Postman Base URL environment variable or use `http://127.0.0.1:8000`.

---

### Postman Test Cases

#### Test Case 1: Create Student (POST)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "register_number": "25AD3099",
    "name": "Kavitha Ramesh",
    "email": "kavitha.r@example.com",
    "phone": "9876501234",
    "date_of_birth": "2005-04-12",
    "gender": "Female",
    "department": "AI&DS",
    "year": "I",
    "section": "A",
    "address": "45 North Street, Coimbatore",
    "admission_date": "2025-08-01",
    "status": "Active"
  }
  ```
- **Expected Status**: `201 Created`
- **Postman Test Assertion**:
  ```javascript
  pm.test("Status code is 201", function () {
      pm.response.to.have.status(201);
  });
  pm.test("Register number matches", function () {
      var jsonData = pm.response.json();
      pm.expect(jsonData.register_number).to.eql("25AD3099");
  });
  ```

---

#### Test Case 2: Get All Students (GET)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Expected Status**: `200 OK`
- **Postman Test Assertion**:
  ```javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });
  ```

---

#### Test Case 3: Get Student by ID (GET)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Expected Status**: `200 OK`
- **Postman Test Assertion**:
  ```javascript
  pm.test("Status code is 200 and has student data", function () {
      pm.response.to.have.status(200);
      var jsonData = pm.response.json();
      pm.expect(jsonData).to.have.property('id');
  });
  ```

---

#### Test Case 4: Update Student (PUT)
- **Method**: `PUT`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "register_number": "25AD3018",
    "name": "Balaji Ramanathan Updated",
    "email": "balaji.new@example.com",
    "phone": "9876543210",
    "date_of_birth": "2005-05-14",
    "gender": "Male",
    "department": "AI&DS",
    "year": "II",
    "section": "A",
    "address": "124 Tech Park, Chennai",
    "admission_date": "2025-08-01",
    "status": "Active"
  }
  ```
- **Expected Status**: `200 OK`

---

#### Test Case 5: Partial Update Student (PATCH)
- **Method**: `PATCH`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "status": "Inactive"
  }
  ```
- **Expected Status**: `200 OK`

---

#### Test Case 6: Delete Student (DELETE)
- **Method**: `DELETE`
- **URL**: `http://127.0.0.1:8000/api/students/1/`
- **Expected Status**: `204 No Content`

---

#### Test Case 7: Invalid Student ID (GET)
- **Method**: `GET`
- **URL**: `http://127.0.0.1:8000/api/students/99999/`
- **Expected Status**: `404 Not Found`

---

#### Test Case 8: Duplicate Register Number (POST)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "register_number": "25CS1002",
    "name": "Another Student",
    "email": "unique.email@example.com",
    "phone": "9876543211",
    "date_of_birth": "2005-01-01",
    "gender": "Male",
    "department": "CSE",
    "year": "I",
    "section": "A",
    "admission_date": "2025-08-01"
  }
  ```
- **Expected Status**: `400 Bad Request`
- **Expected Response**:
  ```json
  {
    "register_number": ["Student with register number '25CS1002' already exists."]
  }
  ```

---

#### Test Case 9: Missing Required Field (POST)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "name": "Incomplete Student"
  }
  ```
- **Expected Status**: `400 Bad Request`

---

#### Test Case 10: Invalid Email Format (POST)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/api/students/`
- **Headers**:
  ```
  Content-Type: application/json
  ```
- **Body (raw JSON)**:
  ```json
  {
    "register_number": "25EC4444",
    "name": "Test Student",
    "email": "not-an-email",
    "phone": "9876543210",
    "date_of_birth": "2005-01-01",
    "admission_date": "2025-08-01"
  }
  ```
- **Expected Status**: `400 Bad Request`
- **Expected Response**:
  ```json
  {
    "email": ["Enter a valid email address."]
  }
  ```
