from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]

admin.site.site_header = "Student Management System Admin"
admin.site.site_title = "SMS Admin Portal"
admin.site.index_title = "Welcome to Student Management Portal"
