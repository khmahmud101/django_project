

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=100)
    sale_price = models.DecimalField(decimal_places=2,max_digits=100,null=True,blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media',null=True)

    class Meta:
        unique_together = ('title','slug')


    def __str__(self):
        return self.title
