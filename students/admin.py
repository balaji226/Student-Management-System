from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'register_number',
        'name',
        'department',
        'year',
        'section',
        'status',
        'email',
        'phone',
        'admission_date',
    )
    list_filter = (
        'department',
        'year',
        'status',
        'gender',
        'admission_date',
    )
    search_fields = (
        'register_number',
        'name',
        'email',
        'phone',
    )
    ordering = ('-created_at',)
    list_per_page = 20
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Academic Details', {
            'fields': (
                'register_number',
                'department',
                'year',
                'section',
                'admission_date',
                'status',
            )
        }),
        ('Personal Information', {
            'fields': (
                'name',
                'date_of_birth',
                'gender',
                'email',
                'phone',
                'address',
            )
        }),
        ('System Timestamps', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at'),
        }),
    )
