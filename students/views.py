from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Student
from .serializers import StudentSerializer


# --------------------------------------------------------------------------
# REST API ViewSet
# --------------------------------------------------------------------------
class StudentViewSet(viewsets.ModelViewSet):
    """
    API ViewSet providing complete CRUD operations for Student records:
    - GET /api/students/ (list with search, department, year, status filters)
    - POST /api/students/ (create new student)
    - GET /api/students/{id}/ (retrieve student detail)
    - PUT /api/students/{id}/ (full update)
    - PATCH /api/students/{id}/ (partial update)
    - DELETE /api/students/{id}/ (delete student)
    - GET /api/students/stats/ (metrics for dashboard)
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        
        # Search across name, register_number, and email
        search_query = self.request.query_params.get('search', '').strip()
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(register_number__icontains=search_query) |
                Q(email__icontains=search_query)
            )

        # Filter by department
        department = self.request.query_params.get('department', '').strip()
        if department:
            queryset = queryset.filter(department__iexact=department)

        # Filter by year
        year = self.request.query_params.get('year', '').strip()
        if year:
            queryset = queryset.filter(year__iexact=year)

        # Filter by status
        status_param = self.request.query_params.get('status', '').strip()
        if status_param:
            queryset = queryset.filter(status__iexact=status_param)

        return queryset

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Return summary metrics for dashboard."""
        total = Student.objects.count()
        active = Student.objects.filter(status='Active').count()
        inactive = total - active
        
        dept_counts = (
            Student.objects.values('department')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        
        return Response({
            'total_students': total,
            'active_students': active,
            'inactive_students': inactive,
            'departments_count': dept_counts.count(),
            'department_breakdown': list(dept_counts)
        })


# --------------------------------------------------------------------------
# Frontend Template Views
# --------------------------------------------------------------------------

def login_view(request):
    """Admin Login View."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html')


def logout_view(request):
    """Admin Logout View."""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('login')


@login_required
def dashboard_view(request):
    """Admin Dashboard View."""
    total_students = Student.objects.count()
    active_students = Student.objects.filter(status='Active').count()
    inactive_students = total_students - active_students

    # Department breakdown
    dept_distribution = (
        Student.objects.values('department')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    departments_count = dept_distribution.count()

    # Calculate percentages for progress bars
    dept_stats = []
    for item in dept_distribution:
        percentage = round((item['count'] / total_students) * 100, 1) if total_students > 0 else 0
        dept_stats.append({
            'department': item['department'],
            'count': item['count'],
            'percentage': percentage
        })

    # Recent 5 students
    recent_students = Student.objects.all()[:5]

    context = {
        'total_students': total_students,
        'active_students': active_students,
        'inactive_students': inactive_students,
        'departments_count': departments_count,
        'dept_stats': dept_stats,
        'recent_students': recent_students,
    }
    return render(request, 'dashboard.html', context)


@login_required
def student_list_view(request):
    """List, search, filter, and paginate students."""
    queryset = Student.objects.all()

    # Search query
    search = request.GET.get('search', '').strip()
    if search:
        queryset = queryset.filter(
            Q(name__icontains=search) |
            Q(register_number__icontains=search) |
            Q(email__icontains=search)
        )

    # Filter parameters
    department = request.GET.get('department', '').strip()
    if department:
        queryset = queryset.filter(department=department)

    year = request.GET.get('year', '').strip()
    if year:
        queryset = queryset.filter(year=year)

    status_filter = request.GET.get('status', '').strip()
    if status_filter:
        queryset = queryset.filter(status=status_filter)

    # Pagination: 10 items per page
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    context = {
        'students': page_obj,
        'page_obj': page_obj,
        'total_count': queryset.count(),
        'departments': Student.DEPARTMENT_CHOICES,
        'years': Student.YEAR_CHOICES,
        'statuses': Student.STATUS_CHOICES,
        'selected_search': search,
        'selected_department': department,
        'selected_year': year,
        'selected_status': status_filter,
    }
    return render(request, 'students.html', context)


@login_required
def student_detail_view(request, pk):
    """View detailed profile of a single student."""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})


@login_required
def student_add_view(request):
    """Create new student record."""
    if request.method == 'POST':
        data = request.POST.copy()
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            student = serializer.save()
            messages.success(request, f"Student '{student.name}' ({student.register_number}) created successfully!")
            return redirect('student_detail', pk=student.pk)
        else:
            # Flatten validation errors to display to user
            for field, err_list in serializer.errors.items():
                for err in err_list:
                    field_name = field.replace('_', ' ').capitalize()
                    messages.error(request, f"{field_name}: {err}")
            return render(request, 'add_student.html', {
                'form_data': data,
                'errors': serializer.errors,
                'departments': Student.DEPARTMENT_CHOICES,
                'years': Student.YEAR_CHOICES,
                'sections': Student.SECTION_CHOICES,
                'genders': Student.GENDER_CHOICES,
                'statuses': Student.STATUS_CHOICES,
            })

    context = {
        'departments': Student.DEPARTMENT_CHOICES,
        'years': Student.YEAR_CHOICES,
        'sections': Student.SECTION_CHOICES,
        'genders': Student.GENDER_CHOICES,
        'statuses': Student.STATUS_CHOICES,
    }
    return render(request, 'add_student.html', context)


@login_required
def student_edit_view(request, pk):
    """Update existing student record."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        data = request.POST.copy()
        serializer = StudentSerializer(student, data=data)
        if serializer.is_valid():
            updated_student = serializer.save()
            messages.success(request, f"Student '{updated_student.name}' updated successfully!")
            return redirect('student_detail', pk=updated_student.pk)
        else:
            for field, err_list in serializer.errors.items():
                for err in err_list:
                    field_name = field.replace('_', ' ').capitalize()
                    messages.error(request, f"{field_name}: {err}")
            return render(request, 'edit_student.html', {
                'student': student,
                'form_data': data,
                'errors': serializer.errors,
                'departments': Student.DEPARTMENT_CHOICES,
                'years': Student.YEAR_CHOICES,
                'sections': Student.SECTION_CHOICES,
                'genders': Student.GENDER_CHOICES,
                'statuses': Student.STATUS_CHOICES,
            })

    context = {
        'student': student,
        'departments': Student.DEPARTMENT_CHOICES,
        'years': Student.YEAR_CHOICES,
        'sections': Student.SECTION_CHOICES,
        'genders': Student.GENDER_CHOICES,
        'statuses': Student.STATUS_CHOICES,
    }
    return render(request, 'edit_student.html', context)


@login_required
def student_delete_view(request, pk):
    """Delete a student record."""
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        reg_no = student.register_number
        name = student.name
        student.delete()
        messages.success(request, f"Student '{name}' ({reg_no}) was deleted successfully.")
        return redirect('student_list')
    
    return redirect('student_detail', pk=pk)
