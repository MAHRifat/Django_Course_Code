from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.roll} - {self.name}"
    
# module inheritance
    # 1. Abstract base class
    # 2. multitable inheritance
    # 3. proxy model
    
# Abstract base class

class CommonInfoClass(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    class Meta:
        abstract = True

class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField(primary_key=True)
    payment = models.IntegerField()
    section = models.CharField(max_length=10)
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()