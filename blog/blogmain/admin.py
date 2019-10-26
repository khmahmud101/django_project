from django.contrib import admin
from .models import *
class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__","details"]
    class Meta:
        Model = Author
admin.site.register(Author,authorModel)

class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]

    list_per_page = 20
    class Meta:
        Model = Category
admin.site.register(Category,categoryModel)

class articleModel(admin.ModelAdmin):
    list_display = ["__str__","posted_on"]
    search_fields = ["__str__", "details"]
    list_filter = ["posted_on","category"]
    list_per_page = 20
    class Meta:
        Model = Article
admin.site.register(Article,articleModel)
