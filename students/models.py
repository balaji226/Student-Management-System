import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('AI&DS', 'Artificial Intelligence & Data Science'),
        ('CSE', 'Computer Science & Engineering'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('EEE', 'Electrical & Electronics Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
    ]

    YEAR_CHOICES = [
        ('I', '1st Year (I)'),
        ('II', '2nd Year (II)'),
        ('III', '3rd Year (III)'),
        ('IV', '4th Year (IV)'),
    ]

    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    # Primary key is auto-increment integer ID
    register_number = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
        verbose_name="Register Number",
        help_text="Unique student registration/roll number (e.g., 25AD3018)"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Full Name"
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name="Email Address"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone Number",
        help_text="10-digit mobile number"
    )
    date_of_birth = models.DateField(
        verbose_name="Date of Birth"
    )
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male',
        verbose_name="Gender"
    )
    department = models.CharField(
        max_length=50,
        choices=DEPARTMENT_CHOICES,
        default='AI&DS',
        verbose_name="Department"
    )
    year = models.CharField(
        max_length=5,
        choices=YEAR_CHOICES,
        default='I',
        verbose_name="Year"
    )
    section = models.CharField(
        max_length=5,
        choices=SECTION_CHOICES,
        default='A',
        verbose_name="Section"
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name="Address"
    )
    admission_date = models.DateField(
        verbose_name="Admission Date",
        default=timezone.now
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='Active',
        verbose_name="Status"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def clean(self):
        super().clean()
        # Clean and validate phone number (at least 10 digits)
        digits_only = re.sub(r'\D', '', self.phone or '')
        if len(digits_only) < 10 or len(digits_only) > 15:
            raise ValidationError({'phone': 'Phone number must contain between 10 and 15 digits.'})
        
        # Date of birth should be in the past
        if self.date_of_birth and self.date_of_birth >= timezone.now().date():
            raise ValidationError({'date_of_birth': 'Date of birth must be a past date.'})

    def __str__(self):
        return f"{self.register_number} - {self.name} ({self.department})"
