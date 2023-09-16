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
    
# Multitable inheritance

class EmployeeModel(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# proxy model  -> akjon attend thaklei onnojon attendence peye jabe

class Friend(models.Model):       # amar friend class e present ache
    school = models.CharField(max_length=30)
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    hw = models.CharField(max_length=40)

class Me(Friend):   # ami ajke class jai nai 
    class Meta:
        proxy = True        
        ordering = ['id']
        
        
# One to One relationship        

class Person(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    email = models.EmailField(max_length=39)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
class Passport(models.Model):
    user = models.OneToOneField(to=Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()

    
