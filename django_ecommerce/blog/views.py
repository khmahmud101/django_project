from django.shortcuts import render

def blogindex(request):
    return render(request,"blog/blog.html")
