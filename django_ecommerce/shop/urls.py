from django.contrib import admin
from django.urls import path
from . views import *

urlpatterns = [
    path("",index,name="shopHome"),
    path("about/",index,name="AboutUs"),
    path("contact/",contact,name="ContactUs"),
    path("tracker",tracker,name="TrackingStatus"),
    path("search/",search,name="Search"),
    path("productview/",productview,name="productview"),
    path("checkout/",checkout,name="Checkout"),
]
