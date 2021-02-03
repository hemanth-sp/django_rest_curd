
from django.urls import path
from .views import *

urlpatterns = [
    path('students', students_list_or_create, name="students_list_or_create"),
    path('students/<int:pk>/', students_get_or_update, name="students_get_or_update"),
]
