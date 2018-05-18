from django.db import models
# Create your models here.
from rolepermissions.roles import assign_role
from django.db.models import Model
from django.contrib.auth.models import AbstractUser,AbstractBaseUser


class Project(models.Model):
     id = models.AutoField(primary_key=True)
     Title = models.TextField()
     Student = models.ForeignKey('Student',on_delete=models.CASCADE,null=True , related_name="Student")
     Professor = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True , related_name="Davar0")
     Detail = models.TextField()
     Requirements = models.TextField()
     TagofProject = models.TextField(null=True)
     status = models.IntegerField()
     ProjectFile = models.TextField(null=True)
     PresentFile = models.TextField(null=True)
     referee1 = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True , related_name="Davar1")
     referee2 = models.ForeignKey('Professor',on_delete=models.CASCADE,null=True , related_name="Davar2")
     DeadlineDate = models.TextField(null=True)
     DeadlineTime = models.IntegerField(null=True)
     Professor_Score = models.FloatField(null=True)
     referee1_Score = models.FloatField(null=True)
     referee2_Score = models.FloatField(null=True)
     final_Score = models.FloatField(null=True)

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

