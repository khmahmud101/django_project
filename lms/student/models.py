from django.db import models


class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    date_of_birth = models.IntegerField()
    user_name = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=200)
    batch = models.IntegerField()
    email = models.CharField(max_length=100,unique=True)
    password1 = models.CharField(max_length=50)
    Password2 = models.CharField(max_length=50)
    phone= models.IntegerField()
    address = models.CharField(max_length=300)

    class Meta:
        abstract = True


class register_student(Student):
    
    def __str__(self):
        return "Name: {} ID: {}".format(self.name,self.student_id)

