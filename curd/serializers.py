from rest_framework import fields, serializers
from .models import *


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'age', 'school', 'created_at']
        read_only_fields = ["id","created_at"]