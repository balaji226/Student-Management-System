import datetime
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from students.models import Student


class Command(BaseCommand):
    help = 'Seeds initial admin superuser and sample student records for demonstration.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Seeding Student Management System database..."))

        # 1. Create or update default admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@sms.edu',
                'first_name': 'System',
                'last_name': 'Administrator',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        admin_user.set_password('admin123')
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("[+] Created superuser: admin / admin123"))
        else:
            self.stdout.write(self.style.SUCCESS("[*] Superuser 'admin' password updated to 'admin123'"))

        # 2. Sample student records
        sample_students = [
            {
                'register_number': '25AD3018',
                'name': 'Balaji R',
                'email': 'balaji@example.com',
                'phone': '9876543210',
                'date_of_birth': datetime.date(2005, 5, 14),
                'gender': 'Male',
                'department': 'AI&DS',
                'year': 'I',
                'section': 'A',
                'address': '124 Tech Park Avenue, Anna Nagar, Chennai',
                'admission_date': datetime.date(2025, 8, 1),
                'status': 'Active'
            },
            {
                'register_number': '25CS1002',
                'name': 'Priya Sharma',
                'email': 'priya.sharma@example.com',
                'phone': '9876543211',
                'date_of_birth': datetime.date(2005, 9, 21),
                'gender': 'Female',
                'department': 'CSE',
                'year': 'I',
                'section': 'A',
                'address': '45 Lake View Road, Gandhinagar, Bangalore',
                'admission_date': datetime.date(2025, 8, 1),
                'status': 'Active'
            },
            {
                'register_number': '24CS1015',
                'name': 'Rahul Verma',
                'email': 'rahul.verma@example.com',
                'phone': '9876543212',
                'date_of_birth': datetime.date(2004, 3, 10),
                'gender': 'Male',
                'department': 'CSE',
                'year': 'II',
                'section': 'B',
                'address': '78 Hill Crest Colony, Hyderabad',
                'admission_date': datetime.date(2024, 7, 20),
                'status': 'Active'
            },
            {
                'register_number': '24IT2008',
                'name': 'Ananya Iyer',
                'email': 'ananya.iyer@example.com',
                'phone': '9876543213',
                'date_of_birth': datetime.date(2004, 11, 28),
                'gender': 'Female',
                'department': 'IT',
                'year': 'II',
                'section': 'A',
                'address': '12 Temple Street, Mylapore, Chennai',
                'admission_date': datetime.date(2024, 7, 25),
                'status': 'Active'
            },
            {
                'register_number': '23EC3042',
                'name': 'Karthik Rajan',
                'email': 'karthik.rajan@example.com',
                'phone': '9876543214',
                'date_of_birth': datetime.date(2003, 7, 19),
                'gender': 'Male',
                'department': 'ECE',
                'year': 'III',
                'section': 'A',
                'address': '89 Cross Cut Road, Coimbatore',
                'admission_date': datetime.date(2023, 8, 5),
                'status': 'Active'
            },
            {
                'register_number': '23EC3011',
                'name': 'Sneha Nair',
                'email': 'sneha.nair@example.com',
                'phone': '9876543215',
                'date_of_birth': datetime.date(2003, 12, 5),
                'gender': 'Female',
                'department': 'ECE',
                'year': 'III',
                'section': 'B',
                'address': '34 Green Garden, Kochi, Kerala',
                'admission_date': datetime.date(2023, 8, 5),
                'status': 'Inactive'
            },
            {
                'register_number': '22EE4005',
                'name': 'Vignesh Kumar',
                'email': 'vignesh.kumar@example.com',
                'phone': '9876543216',
                'date_of_birth': datetime.date(2002, 4, 15),
                'gender': 'Male',
                'department': 'EEE',
                'year': 'IV',
                'section': 'A',
                'address': '55 Ring Road, Madurai',
                'admission_date': datetime.date(2022, 9, 10),
                'status': 'Active'
            },
            {
                'register_number': '25AD3024',
                'name': 'Divya Krishnan',
                'email': 'divya.krishnan@example.com',
                'phone': '9876543217',
                'date_of_birth': datetime.date(2005, 1, 30),
                'gender': 'Female',
                'department': 'AI&DS',
                'year': 'I',
                'section': 'B',
                'address': '201 Sun City, Velachery, Chennai',
                'admission_date': datetime.date(2025, 8, 1),
                'status': 'Active'
            },
            {
                'register_number': '24ME2019',
                'name': 'Mohammed Farhan',
                'email': 'farhan.m@example.com',
                'phone': '9876543218',
                'date_of_birth': datetime.date(2004, 6, 8),
                'gender': 'Male',
                'department': 'MECH',
                'year': 'II',
                'section': 'A',
                'address': '62 Industrial Estate, Salem',
                'admission_date': datetime.date(2024, 8, 12),
                'status': 'Active'
            },
            {
                'register_number': '23CV3003',
                'name': 'Harini Sundar',
                'email': 'harini.s@example.com',
                'phone': '9876543219',
                'date_of_birth': datetime.date(2003, 8, 22),
                'gender': 'Female',
                'department': 'CIVIL',
                'year': 'III',
                'section': 'A',
                'address': '9 West Boulevard, Tiruchirappalli',
                'admission_date': datetime.date(2023, 8, 2),
                'status': 'Active'
            },
        ]

        count = 0
        for item in sample_students:
            student, created = Student.objects.update_or_create(
                register_number=item['register_number'],
                defaults=item
            )
            if created:
                count += 1

        self.stdout.write(self.style.SUCCESS(f"[+] Successfully seeded {len(sample_students)} students ({count} new)."))
        self.stdout.write(self.style.SUCCESS("Database is ready! Login with username 'admin' and password 'admin123'."))
