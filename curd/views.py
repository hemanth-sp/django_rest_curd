from rest_framework.views import APIView
from curd.serializers import StudentSerializers
from curd.models import Student
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]


class StudentCurdd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]