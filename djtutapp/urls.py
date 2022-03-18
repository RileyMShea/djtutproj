from django.urls import path
from .views import StudentList, index

urlpatterns = [
    path('', index, name='student_index'),
    path('student/', StudentList.as_view(), name='student_list'),
]
