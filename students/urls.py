from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from students.views import (create_student, get_students, get_student, update_student,
                            delete_student, partial_update_student, get_branch)

urlpatterns = [
    # JWT Authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # CRUD API endpoints
    path('students/create/', create_student, name='create-student'),
    path('students/', get_students, name='get-students'),
    path('students/<int:student_id>/', get_student, name='get-student'),
    path('students/update/<int:student_id>/', update_student, name='update-student'),
    path('students/delete/<int:student_id>/', delete_student, name='delete-student'),
    path('students/patch/<int:student_id>/', partial_update_student, name='patch-student'),
    path('students/branch/', get_branch, name='get-branch'),
]
