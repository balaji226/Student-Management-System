import re
from rest_framework import serializers
from django.utils import timezone
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'register_number',
            'name',
            'email',
            'phone',
            'date_of_birth',
            'gender',
            'department',
            'year',
            'section',
            'address',
            'admission_date',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_register_number(self, value):
        value = value.strip().upper()
        if not value:
            raise serializers.ValidationError("Register number cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Register number must be at least 3 characters long.")
        
        # Check uniqueness during create or update
        instance = getattr(self, 'instance', None)
        existing = Student.objects.filter(register_number__iexact=value)
        if instance:
            existing = existing.exclude(pk=instance.pk)
        if existing.exists():
            raise serializers.ValidationError(f"Student with register number '{value}' already exists.")
        return value

    def validate_email(self, value):
        value = value.strip().lower()
        instance = getattr(self, 'instance', None)
        existing = Student.objects.filter(email__iexact=value)
        if instance:
            existing = existing.exclude(pk=instance.pk)
        if existing.exists():
            raise serializers.ValidationError(f"A student with email '{value}' already exists.")
        return value

    def validate_phone(self, value):
        value = value.strip()
        digits = re.sub(r'\D', '', value)
        if len(digits) < 10 or len(digits) > 15:
            raise serializers.ValidationError("Phone number must contain between 10 and 15 digits.")
        return digits

    def validate_date_of_birth(self, value):
        if value and value >= timezone.now().date():
            raise serializers.ValidationError("Date of birth must be a past date.")
        return value

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Student name cannot be empty.")
        if len(value) < 2:
            raise serializers.ValidationError("Student name must have at least 2 characters.")
        return value
