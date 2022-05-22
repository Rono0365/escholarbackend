from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=100,default='')
class homework(models.Model):
    name = models.CharField(max_length=100,default = 'no homework')
    Class = models.ManyToManyField('Class')
    #subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    deadline = models.CharField(max_length=100,default = '')
    #students = models.ManyToManyField('Student')
    
class Class(models.Model):
    name = models.CharField(max_length=100,default = '')  
    students = models.ManyToManyField('Student')
    
    #subject = models.ManyToManyField(Student)
class Student(models.Model):
    #created = models.DateTimeField(auto_now_add=True)
    School = models.ForeignKey(School,on_delete=models.CASCADE, default='')
    #Class = models.ForeignKey(Class,on_delete=models.CASCADE, default='')
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='')
    
    adm_no = models.CharField(max_length=100, blank=True, default='')
    Subjects =  models.ManyToManyField('Subject',default='')
    
    class Meta:
        ordering = ['adm_no']
class Teacher(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    #created = models.DateTimeField(auto_now_add=True)
    School = models.ForeignKey(School,default = '',on_delete=models.CASCADE)
    #Subjectz = models.ForeignKey('Subject',default = '',on_delete=models.CASCADE)
    adm_no = models.CharField(max_length=100, blank=True, default='')
    #Subjects =  models.ForeignKey(SubjectsV,default = '',on_delete=models.CASCADE)
    class Meta:
        ordering = ['first_name']

#blank=True
class Subject(models.Model):
    headline = models.CharField(max_length=100)
    #n_students = models.ManyToManyField(Student,default='')
    day_taught = models.CharField(max_length=100)#self arrange in the timetable
    time_taught = models.CharField(max_length=100)#self arrange in the timetable
    time_duration = models.CharField(max_length=100)#self arrange in the timetable
    #grade = models.CharField(max_length=100)#self arrange in the timetable
    
    place_taught = models.CharField(max_length=100)#self arrange in the timetable
    #homework = models.ForeignKey(homework,default = '',on_delete=models.CASCADE)
    code =models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    
    
    class Meta:
        ordering = ['headline']

    
