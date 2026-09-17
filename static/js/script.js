/**
 * Student Management System - Client-side Logic & Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------------------
    // 1. Toast Notification Auto-Dismissal
    // -------------------------------------------------------------------------
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        const timer = setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(() => toast.remove(), 300);
        }, 4500);

        const closeBtn = toast.querySelector('.toast-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                clearTimeout(timer);
                toast.style.opacity = '0';
                toast.style.transform = 'translateX(100%)';
                setTimeout(() => toast.remove(), 300);
            });
        }
    });

    // -------------------------------------------------------------------------
    // 2. Delete Confirmation Modal
    // -------------------------------------------------------------------------
    const deleteModal = document.getElementById('deleteModal');
    const deleteForm = document.getElementById('deleteForm');
    const studentNameSpan = document.getElementById('deleteStudentName');
    const studentRegSpan = document.getElementById('deleteStudentReg');
    const cancelDeleteBtn = document.getElementById('cancelDeleteBtn');
    const closeDeleteModalBtn = document.getElementById('closeDeleteModalBtn');

    window.openDeleteModal = function(id, name, regNo) {
        if (!deleteModal || !deleteForm) return;
        deleteForm.action = `/students/${id}/delete/`;
        if (studentNameSpan) studentNameSpan.textContent = name;
        if (studentRegSpan) studentRegSpan.textContent = regNo;
        deleteModal.classList.add('show');
    };

    function closeDeleteModal() {
        if (deleteModal) deleteModal.classList.remove('show');
    }

    if (cancelDeleteBtn) cancelDeleteBtn.addEventListener('click', closeDeleteModal);
    if (closeDeleteModalBtn) closeDeleteModalBtn.addEventListener('click', closeDeleteModal);

    if (deleteModal) {
        deleteModal.addEventListener('click', (e) => {
            if (e.target === deleteModal) closeDeleteModal();
        });
    }

    // -------------------------------------------------------------------------
    // 3. Form Validation for Student Creation & Modification
    // -------------------------------------------------------------------------
    const studentForm = document.getElementById('studentForm');
    if (studentForm) {
        studentForm.addEventListener('submit', (e) => {
            let isValid = true;

            const nameInput = document.getElementById('name');
            const regInput = document.getElementById('register_number');
            const emailInput = document.getElementById('email');
            const phoneInput = document.getElementById('phone');
            const dobInput = document.getElementById('date_of_birth');

            // Reset error states
            studentForm.querySelectorAll('.form-control').forEach(el => el.classList.remove('is-invalid'));

            // Name check
            if (nameInput && nameInput.value.trim().length < 2) {
                showFieldError(nameInput, "Please enter a valid student name (minimum 2 characters).");
                isValid = false;
            }

            // Register number check
            if (regInput && regInput.value.trim().length < 3) {
                showFieldError(regInput, "Register number must have at least 3 characters.");
                isValid = false;
            }

            // Email check
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailInput && !emailRegex.test(emailInput.value.trim())) {
                showFieldError(emailInput, "Please enter a valid email address (e.g., student@example.com).");
                isValid = false;
            }

            // Phone check (10 digits)
            const phoneRegex = /^[0-9]{10,15}$/;
            const cleanedPhone = phoneInput ? phoneInput.value.replace(/\D/g, '') : '';
            if (phoneInput && !phoneRegex.test(cleanedPhone)) {
                showFieldError(phoneInput, "Please enter a valid 10 to 15 digit mobile number.");
                isValid = false;
            }

            // Date of birth check (must be in past)
            if (dobInput && dobInput.value) {
                const dobDate = new Date(dobInput.value);
                const today = new Date();
                if (dobDate >= today) {
                    showFieldError(dobInput, "Date of birth must be a date in the past.");
                    isValid = false;
                }
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    function showFieldError(inputElement, message) {
        inputElement.classList.add('is-invalid');
        const feedback = inputElement.parentElement.querySelector('.invalid-feedback');
        if (feedback) {
            feedback.textContent = message;
            feedback.style.display = 'block';
        }
    }

    // -------------------------------------------------------------------------
    // 4. Filter Toolbar Interactions & Debounced Search
    // -------------------------------------------------------------------------
    const filterForm = document.getElementById('filterForm');
    if (filterForm) {
        const selects = filterForm.querySelectorAll('.select-filter');
        selects.forEach(select => {
            select.addEventListener('change', () => filterForm.submit());
        });

        const searchInput = filterForm.querySelector('.search-input');
        if (searchInput) {
            let debounceTimer;
            searchInput.addEventListener('input', () => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {
                    filterForm.submit();
                }, 500);
            });
        }
    }

    // -------------------------------------------------------------------------
    // 5. Mobile Sidebar Toggle
    // -------------------------------------------------------------------------
    const sidebarToggle = document.getElementById('sidebarToggle');
    const sidebar = document.querySelector('.sidebar');
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }
});

// Helper for 1-Click Demo Login credentials fill
window.fillDemoCredentials = function() {
    const userInput = document.getElementById('username');
    const passInput = document.getElementById('password');
    if (userInput && passInput) {
        userInput.value = 'admin';
        passInput.value = 'admin123';
        userInput.focus();
    }
};
