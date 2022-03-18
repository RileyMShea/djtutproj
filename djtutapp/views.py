from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


class StudentList(APIView):
    """
    List all students, or create a new student.
    """

    def get(self, request, format=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
