from curd.serializers import StudentSerializers
from curd.models import Student
from rest_framework import permissions, generics, viewsets


class StudentCurd(viewsets.ViewSetMixin, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    permission_classes = [permissions.AllowAny]
