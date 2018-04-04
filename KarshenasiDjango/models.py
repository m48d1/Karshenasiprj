from django.db import models
# Create your models here.
from rolepermissions.roles import assign_role
from django.db.models import Model
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


class Project(models.Model):
     id = models.AutoField(primary_key=True)
     Title = models.TextField()
     StudentNumber = models.IntegerField()
     Professor = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True)
     Detail = models.TextField()
     Requirements = models.TextField()
     TagofProject = models.TextField()
     status = models.IntegerField()

class Professor(models.Model) :
    id = models.AutoField(primary_key=True)
    FullName = models.TextField(null=False)
    MobilePhone = models.TextField(null=False)
    Group = models.TextField(null=True)

class Student(models.Model) :
    id = models.AutoField(primary_key=True)
    FullName = models.TextField(null=False)
    MobilePhone = models.TextField(null=False)
    StudentField = models.IntegerField(null=False)
    StudentUnits = models.IntegerField(null=True)
    StudentNumber = models.IntegerField(null=True)
    StudentPrf = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True)

class User(AbstractUser) :
     id = models.AutoField(primary_key=True)
     Student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True)
     Professor = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True)

