from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Student

class StudentTests(APITestCase):
    def setUp(self):
        self.data = {
            "name": "suresh",
            "age": 11,
            "school": "govt",
        }
        self.response = self.client.post(
            reverse('curd:students-list'),
            self.data,
            format="json")


    def test_api_create_student(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'suresh')

    def test_api_list_students(self):
        url = reverse('curd:students-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 1)

    def test_api_can_get_a_student(self):
        student = Student.objects.get()
        response = self.client.get(
            reverse('curd:students-detail',
            kwargs={'pk': student.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, student)

    def test_api_can_update_a_student(self):
        student = Student.objects.get()
        new_data = {
            "name": "virat",
            "age": 11,
            "school": "govt",
        }
        response = self.client.put(
            reverse('curd:students-detail',
            kwargs={'pk': student.id}), data=new_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.get().name, 'virat')

    def test_api_can_delete_a_student(self):
        student = Student.objects.get()
        response = self.client.delete(
            reverse('curd:students-detail',
            kwargs={'pk': student.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)