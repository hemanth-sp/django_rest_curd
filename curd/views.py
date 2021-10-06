from curd.serializers import StudentSerializers
from curd.models import Student
from rest_framework import permissions, generics


class StudentCurd(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]


class StudentCurdd(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]