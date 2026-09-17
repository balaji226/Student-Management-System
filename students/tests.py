import datetime
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student


class StudentModelTest(TestCase):
    """Test cases for Student model methods and constraints."""

    def setUp(self):
        self.student = Student.objects.create(
            register_number="25AD3018",
            name="Balaji R",
            email="balaji@example.com",
            phone="9876543210",
            date_of_birth=datetime.date(2005, 5, 14),
            gender="Male",
            department="AI&DS",
            year="I",
            section="A",
            address="Chennai, India",
            admission_date=datetime.date(2025, 8, 1),
            status="Active"
        )

    def test_student_str(self):
        expected_str = f"{self.student.register_number} - {self.student.name} ({self.student.department})"
        self.assertEqual(str(self.student), expected_str)

    def test_student_defaults(self):
        self.assertEqual(self.student.status, "Active")
        self.assertEqual(self.student.department, "AI&DS")


class StudentAPITest(APITestCase):
    """Test cases for Student REST API endpoints."""

    def setUp(self):
        self.student1 = Student.objects.create(
            register_number="25AD3018",
            name="Balaji R",
            email="balaji@example.com",
            phone="9876543210",
            date_of_birth=datetime.date(2005, 5, 14),
            gender="Male",
            department="AI&DS",
            year="I",
            section="A",
            address="Anna Nagar, Chennai",
            admission_date=datetime.date(2025, 8, 1),
            status="Active"
        )
        self.student2 = Student.objects.create(
            register_number="25CS1002",
            name="Priya Sharma",
            email="priya@example.com",
            phone="9876543211",
            date_of_birth=datetime.date(2005, 9, 21),
            gender="Female",
            department="CSE",
            year="I",
            section="A",
            address="Bangalore, Karnataka",
            admission_date=datetime.date(2025, 8, 1),
            status="Inactive"
        )
        self.list_url = reverse('student-api-list')

    def test_get_all_students(self):
        """GET /api/students/ should return all student records."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # DRF pagination wrapped in results
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 2)

    def test_get_student_detail(self):
        """GET /api/students/{id}/ should return student details."""
        url = reverse('student-api-detail', kwargs={'pk': self.student1.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['register_number'], "25AD3018")
        self.assertEqual(response.data['name'], "Balaji R")

    def test_create_student_success(self):
        """POST /api/students/ should create a new student record."""
        payload = {
            "register_number": "24IT2008",
            "name": "Ananya Iyer",
            "email": "ananya@example.com",
            "phone": "9876543213",
            "date_of_birth": "2004-11-28",
            "gender": "Female",
            "department": "IT",
            "year": "II",
            "section": "A",
            "address": "Mylapore, Chennai",
            "admission_date": "2024-07-25",
            "status": "Active"
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 3)
        self.assertEqual(response.data['register_number'], "24IT2008")

    def test_create_duplicate_register_number(self):
        """POST /api/students/ with duplicate register number should return 400."""
        payload = {
            "register_number": "25AD3018",  # duplicate
            "name": "Another Student",
            "email": "another@example.com",
            "phone": "9876543299",
            "date_of_birth": "2005-01-01",
            "gender": "Male",
            "department": "AI&DS",
            "year": "I",
            "section": "A",
            "admission_date": "2025-08-01",
            "status": "Active"
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('register_number', response.data)

    def test_create_duplicate_email(self):
        """POST /api/students/ with duplicate email should return 400."""
        payload = {
            "register_number": "25ME9999",
            "name": "Another Student",
            "email": "balaji@example.com",  # duplicate email
            "phone": "9876543299",
            "date_of_birth": "2005-01-01",
            "gender": "Male",
            "department": "MECH",
            "year": "I",
            "section": "A",
            "admission_date": "2025-08-01",
            "status": "Active"
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_invalid_phone_number(self):
        """POST /api/students/ with invalid phone (<10 digits) should return 400."""
        payload = {
            "register_number": "25EE8888",
            "name": "Test Student",
            "email": "test@example.com",
            "phone": "12345",  # too short
            "date_of_birth": "2005-01-01",
            "gender": "Male",
            "department": "EEE",
            "year": "I",
            "section": "A",
            "admission_date": "2025-08-01",
            "status": "Active"
        }
        response = self.client.post(self.list_url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('phone', response.data)

    def test_update_student_put(self):
        """PUT /api/students/{id}/ should completely update the student."""
        url = reverse('student-api-detail', kwargs={'pk': self.student1.pk})
        payload = {
            "register_number": "25AD3018",
            "name": "Balaji Ramanathan",  # updated
            "email": "balaji.updated@example.com",  # updated
            "phone": "9998887776",  # updated
            "date_of_birth": "2005-05-14",
            "gender": "Male",
            "department": "AI&DS",
            "year": "II",  # promoted
            "section": "B",
            "address": "OMR, Chennai",
            "admission_date": "2025-08-01",
            "status": "Active"
        }
        response = self.client.put(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.name, "Balaji Ramanathan")
        self.assertEqual(self.student1.year, "II")

    def test_partial_update_patch(self):
        """PATCH /api/students/{id}/ should update selected fields."""
        url = reverse('student-api-detail', kwargs={'pk': self.student1.pk})
        payload = {"status": "Inactive"}
        response = self.client.patch(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student1.refresh_from_db()
        self.assertEqual(self.student1.status, "Inactive")

    def test_delete_student(self):
        """DELETE /api/students/{id}/ should delete the student."""
        url = reverse('student-api-detail', kwargs={'pk': self.student2.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.filter(pk=self.student2.pk).count(), 0)

    def test_search_by_name(self):
        """GET /api/students/?search=Priya should return matching student."""
        response = self.client.get(self.list_url, {'search': 'Priya'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['register_number'], "25CS1002")

    def test_filter_by_department(self):
        """GET /api/students/?department=AI&DS should filter by department."""
        response = self.client.get(self.list_url, {'department': 'AI&DS'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['department'], "AI&DS")

    def test_stats_endpoint(self):
        """GET /api/students/stats/ should return total, active, and inactive counts."""
        url = reverse('student-api-stats')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_students'], 2)
        self.assertEqual(response.data['active_students'], 1)
        self.assertEqual(response.data['inactive_students'], 1)
