from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name','last_name','School','adm_no','Subjectz']
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name']
class SubjectSerializer(serializers.ModelSerializer):
    #homework = serializers.ReadOnlyField(source='homework.name')    
    class Meta:
        unique_together = (('headline','day_taught','time_duration','time_taught','code','teacher','place_taught'),)
        model = Subject
        fields = ['headline','day_taught','time_duration','time_taught','code','teacher','place_taught']
class UserSerializer(serializers.ModelSerializer):
    #homework = serializers.ReadOnlyField(source='homework.name')
    #Subjects = serializers.SerializerMethodField('Subject.headline')
    #firstname = serializers.ReadOnlyField(source='User.first_name')
    Subjects = SubjectSerializer(many=True)
    Class = serializers.ReadOnlyField(source='Class.name')
    School = serializers.ReadOnlyField(source='School.name')
    firstname = serializers.ReadOnlyField(source='owner.first_name')#owner.username
    lastname = serializers.ReadOnlyField(source='owner.last_name')
    
    class Meta:
         model = Student
         fields = ['School','adm_no','firstname','lastname','Class','Subjects']

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name']
class HomeworkSerializer(serializers.ModelSerializer):
    # = serializers.ReadOnlyField(source='Class.name')
    #name = serializers.ReadOnlyField(source='Subject.headline')#headline
    Class = serializers.ReadOnlyField(source='Class.name')
    #homework = serializers.ReadOnlyField(source='homework.name')    
    class Meta:
        model = homework
        fields = ['name','deadline']        
class RegisterSerializer(serializers.ModelSerializer,):
    permission_classes = []
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user                