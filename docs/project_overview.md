# Project Overview: Student Management System (SMS)

## 1. Project Title
**Student Management System (SMS)** — A Modern Full-Stack CRUD Web Application.

---

## 2. Problem Statement
Educational institutions frequently grapple with fragmented, manual, or paper-based student record maintenance. Tracking personal details, enrollment years, departments, contact numbers, and status transitions across disparate spreadsheets or ledgers leads to:
- Data redundancy and human clerical errors.
- Slow retrieval during audits, examinations, and departmental inquiries.
- Lack of role-based security and centralized data validation.
- Inability to quickly filter or search large batches of students.

---

## 3. Project Objectives
The objective of this project is to build a robust, intuitive, and secure centralized web portal that enables college administrators to:
1. **Create** new student profiles with strict client-side and server-side validations.
2. **Read** student directories with instant pagination, department classification, and status badges.
3. **Update** student demographic and academic records seamlessly.
4. **Delete** obsolete student entries with safety confirmation dialogs to prevent accidental data loss.
5. **Search & Filter** records dynamically across student name, registration number, email, department, study year, and status.
6. **Expose REST APIs** (`/api/students/`) supporting integration with third-party institutional apps, mobile frontends, and automated testing tools.

---

## 4. Technology Stack & Rationale

| Layer | Technology | Rationale |
|---|---|---|
| **Frontend UI** | HTML5, CSS3, Vanilla JavaScript | Fast, zero dependency build step, highly customizable, responsive layout across mobile and desktop. |
| **Backend Framework** | Python 3.14, Django 6.1 | High-level MVC/MVT framework, built-in ORM, secure session authentication, and automated admin panel. |
| **API Layer** | Django REST Framework (DRF) 3.18 | Industry-standard serializer validation, content negotiation, pagination, and status code compliance. |
| **Database** | SQLite 3 | Embedded, lightweight, zero-configuration relational database ideal for college demonstration and testing. |
| **API Testing** | Postman & Django APITestCase | Comprehensive endpoint validation for all CRUD actions, error scenarios, and status codes. |
| **Version Control** | Git & GitHub | Clean commit milestones, collaboration, and project submission readiness. |

---

## 5. System Architecture & Flow

```
                      +-----------------------------+
                      |         WEB BROWSER         |
                      |  - Modern Responsive UI     |
                      |  - Live Search & Filtering  |
                      |  - Client Validation Regex  |
                      +--------------+--------------+
                                     |
                                     | HTTP Requests (Forms & JSON Fetch)
                                     v
                      +-----------------------------+
                      |       DJANGO BACKEND        |
                      |  - URL Router               |
                      |  - Session Auth Middleware  |
                      |  - Views & DRF ViewSets     |
                      |  - Serializer Validation    |
                      +--------------+--------------+
                                     |
                                     | Python Django ORM
                                     v
                      +-----------------------------+
                      |      SQLITE 3 DATABASE      |
                      |  - students_student table   |
                      |  - Unique constraints       |
                      |  - Transactional integrity  |
                      +-----------------------------+
```

---

## 6. Key Features Summary
1. **Executive Dashboard**:
   - Total Students, Active Count, Inactive Count, Department Count cards.
   - Dynamic department enrollment distribution bars.
   - Quick Add Student launcher.
   - Recent Admissions table preview.
2. **Comprehensive Student CRUD**:
   - Student ID, Register Number, Name, Email, Phone, DOB, Gender, Department, Year, Section, Address, Admission Date, Status.
   - In-app detail card with printable institutional profile view.
3. **Dynamic Search & Multi-Criteria Filtering**:
   - Debounced search querying Name, Register Number, and Email simultaneously.
   - Dropdown filters for Department, Year of Study, and Status.
4. **Safety & Validation**:
   - 10-15 digit phone validation.
   - Strict email regex checks.
   - Duplicate registration number and duplicate email prevention on both client and database levels.
   - Modal prompt before deleting any record.
