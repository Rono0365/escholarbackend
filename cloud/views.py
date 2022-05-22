from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import Student
from .models import Teacher
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            #'email': user.email
        })
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()
class SchoolList(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    def perform_create(self, serializer):
        serializer.save()

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    #permission_classes = (AllowAny,)
    serializer_class = SubjectSerializer

    def perform_create(self, serializer):
        serializer.save()
class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
class ClassList(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def perform_create(self, serializer):
        serializer.save()
class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def perform_create(self, serializer):
        serializer.save()
class homeworkList(generics.ListCreateAPIView):
    queryset = homework.objects.all()
    serializer_class = HomeworkSerializer

    def perform_create(self, serializer):
        serializer.save()
class homeworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = homework.objects.all()
    serializer_class = HomeworkSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = UserSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer          

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
