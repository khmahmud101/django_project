from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    details = models.TextField()
    #author_profile = models.FileField()
    def __str__(self):
        return self.name.username
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=300)
    article_author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.FileField()
    body = models.TextField()
    posted_on = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,auto_now_add=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
