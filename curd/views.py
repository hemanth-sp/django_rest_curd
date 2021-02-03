from curd.serializers import StudentSerializers
from curd.models import Student
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def students_list_or_create(request):
    if request.method == "GET":
        students_qs = Student.objects.all()
        student_serializers = StudentSerializers(students_qs, many=True)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    else:
        student_serializers = StudentSerializers(data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def students_get_or_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == "GET":
        student_serializers = StudentSerializers(student)
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        student_serializers = StudentSerializers(instance=student, data=request.data)
        student_serializers.is_valid(raise_exception=True)
        student_serializers.save()
        return Response(student_serializers.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        student.delete()
        return Response({'msg': 'done'}, status=status.HTTP_204_NO_CONTENT)
