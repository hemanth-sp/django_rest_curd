from rest_framework.views import APIView
from curd.serializers import StudentSerializers
from curd.models import Student
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class StudentCurd(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None, format=None):
        if pk:
            student = get_object_or_404(Student, id=pk)
            student_serializers = StudentSerializers(student)
            return Response(student_serializers.data, status=status.HTTP_200_OK)
        else:
            students_qs = Student.objects.all()
            student_serializers = StudentSerializers(students_qs, many=True)
            return Response(student_serializers.data, status=status.HTTP_200_OK)

    def post(self, request):
        student_serializers = StudentSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk=None, format=None):
        student = get_object_or_404(Student, id=pk)
        student_serializers = StudentSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)

    def delete(self,request, pk=None, format=None):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
