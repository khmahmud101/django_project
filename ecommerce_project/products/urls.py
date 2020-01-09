from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path("",home,name="home"),
    path("products/",all,name="products"),
    path("products/<slug>/",single_product,name="single_product")
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)