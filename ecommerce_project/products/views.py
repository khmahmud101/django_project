from django.shortcuts import render,Http404
from .models import Product
def home(request):
    products = Product.objects.all()
    context ={
        "products": products
    }
    return render(request,"home.html",context)

def all(request):
    products = Product.objects.all()
    #print(products)
    context = {"products":products}
    return render(request,"all.html",context)

def single_product(request,slug):
    try:
        product = Product.objects.get(slug=slug)


        context = {"product":product}
        return render(request,"single.html",context)
    except:
        raise Http404



