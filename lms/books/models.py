from django.db import models
from department.models import * 


class AddBook(models.Model):

    book_name = models.CharField(max_length=200)
    writer_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    course = models.ForeignKey(Degree,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name,self.department


