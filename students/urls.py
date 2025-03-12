from django.urls import path
from oauth2_provider.views import TokenView
from .views import create_student, get_students, get_student, update_student, delete_student, partial_update_student, get_branch

urlpatterns = [
    path('o/token/', TokenView.as_view(), name='token'), #oauth authorization
    path('students/create/', create_student, name='create-student'),  # Create
    path('students/', get_students, name='get-students'),  # Read All
    path('students/<int:student_id>/', get_student, name='get-student'),  # Read Single
    path('students/update/<int:student_id>/', update_student, name='update-student'),  # Update
    path('students/delete/<int:student_id>/', delete_student, name='delete-student'),  # Delete
    path('students/patch/<int:student_id>/', partial_update_student, name='patch-student'), #patch
    path('students/branch/', get_branch, name='get-branch'), #branch
]










# from django.urls import path
# from .views import StudentListCreateAPI, StudentDetailAPI
#
#
# urlpatterns = [
#     path('students/', StudentListCreateAPI.as_view(), name='student-list-create'),
#     path('students/<int:student_id>/', StudentDetailAPI.as_view(), name='student-detail'),
#  ]
