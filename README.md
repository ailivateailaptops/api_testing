# 📌 Student Management API - Testing Guide  

This repository contains the **API testing documentation** for the **Student Management API**. The API provides CRUD operations for managing student data, ensuring proper validations, error handling, and comprehensive testing.  

---

## 🚀 Features of API Testing  

### ✅ **Comprehensive CRUD Operations Testing**  
- **Create Student (POST):**  
  - Validates successful student creation.  
  - Handles duplicate emails and missing fields.  

- **Retrieve Students (GET):**  
  - Tests fetching all students.  
  - Handles cases when no data exists (returns an empty list).  

- **Retrieve Student by ID (GET):**  
  - Ensures correct data retrieval.  
  - Checks error handling for non-existent students.  

- **Update Student (PUT/PATCH):**  
  - Validates full/partial updates.  
  - Enforces validation constraints.  

- **Delete Student (DELETE):**  
  - Ensures proper student deletion.  
  - Handles invalid ID scenarios.  

---

### 🔎 **Validation & Edge Case Testing**  
- **Age Validation:**  
  - Rejects negative values.  
  - Restricts age to a maximum of 120.  

- **Grade Validation:**  
  - Restricts input to predefined values (A, A+, B, B+, etc.).  

- **Email Uniqueness:**  
  - Prevents duplicate email entries.  

- **URL Validation:**  
  - Ensures proper URL format if applicable.  

---

### 📌 **Error Handling & Status Codes Verification**  
- **400 (Bad Request):** Returned for invalid inputs.  
- **404 (Not Found):** Returned for non-existent student records.  
- **200 (OK):** Successful fetch operations.  
- **201 (Created):** Successful student creation.  
- **204 (No Content):** Successful deletion.  

---

### 🔄 **Postman API Testing Collection**  
- **Pre-configured API Requests** for testing all endpoints.  
- **Automated API Tests** with response validation.  
- **Edge Case Scenarios** covered in test scripts.  

---

### 📌 **Database & Migration Testing**  
- Ensures database integrity after migrations.  
- Prevents missing column errors after schema changes.  

---

## 📂 API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/api/students/create/` | Create a new student |
| **GET** | `/api/students/` | Fetch all students |
| **GET** | `/api/students/<id>/` | Fetch a student by ID |
| **PUT** | `/api/students/update/<id>/` | Update student details |
| **PATCH** | `/api/students/patch/<id>/` | Partially update student details |
| **DELETE** | `/api/students/delete/<id>/` | Delete a student by ID |
| **GET** | `/api/students/branch/` | Always returns an empty list |
| **Admin Panel** | `/admin/` | to generate client Id  |
| **Acess-Token** | `/o/token` | to generate acess-token  |
---

## 🛠️ How to Run Tests with oauth2.0
### Install dependencies
  -pip install django
  -pip install django-oauth-toolkit

### 1️⃣ **Using Postman (Manual Testing)**  
1. Import the **Postman Collection and environment variable**.  
2. Run requests for each endpoint.  
3. Verify responses and status codes.  

### 2️⃣ **Running Server**  
```bash
python manage.py runserver

# License
This project is licensed under the MIT License.
