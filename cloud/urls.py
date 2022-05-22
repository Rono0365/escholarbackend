from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from cloud import views
#from transit import *
#from elearn import *


urlpatterns = [
    path('students/', views.StudentList.as_view()),
    path('student/<int:pk>/', views.StudentDetail.as_view()),
    path('subject/<int:pk>/', views.SubjectDetail.as_view()),
    path('homework/<int:pk>/', views.homeworkDetail.as_view()),
    path('teachers/', views.TeacherList.as_view()),
    path('Schools/', views.SchoolList.as_view()),
    path('Subjects/', views.SubjectList.as_view()),
    path('classes/', views.ClassList.as_view()),
    path('homework/', views.homeworkList.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    
    
]


