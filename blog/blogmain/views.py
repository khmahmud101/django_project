from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from .forms import *

def index(request):
    posts = Article.objects.all()
    context={
        "posts":posts
    }
    return render(request,"index.html",context)

def profile(request,name):
    post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author,name=post_author.id)
    post = Article.objects.filter(article_author=auth.id)
    context={
        "auth":auth,
        "post":post
    }
    return render(request,"profile.html",context)

def single_post(request,id):
    post = get_object_or_404(Article,pk=id)
    first=Article.objects.first()
    last=Article.objects.last()
    related = Article.objects.filter(category=post.category).exclude(id=id)[:4]
    context={
        "post":post,
        "first":first,
        "last":last,
        "related":related,
    }
    return render(request,"single.html",context)

def category(request, name):
    cat = get_object_or_404(Category,name=name)
    post=Article.objects.filter(category=cat.id)

    return render(request,"category.html",{"post":post,"cat":cat})

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request,username=user,password=password)
            if auth is not None:
                login(request,auth)
                return redirect('index')

    return render(request,"login.html")

def getlogout(request):
    logout(request)
    return redirect('index')


def create(request):
    if request.user.is_authenticated:
        you = get_object_or_404(Author, name=request.user.id)
        form=createform(request.POST or None,request.FILES or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.article_author = you
            instance.save()
            return redirect('index')
        return render(request,"create.html",{"form":form})
    else:
        return redirect('login')


def author_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(Author, name=request.user.id)
        post = Article.objects.filter(article_author= user.id)
        return render(request,"author-profile.html",{"post":post,"user":user})
    else:
        return redirect('login')


def getupdate(request,id):
    if request.user.is_authenticated:
        you = get_object_or_404(Author, name=request.user.id)
        post=get_object_or_404(Article,id=id)
        form=createform(request.POST or None,request.FILES or None, instance=post)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.article_author = you
            instance.save()
            return redirect('author_profile')
        return render(request,"create.html",{"form":form})
    else:
        return redirect('login')


def getdelete(request,id):
    if request.user.is_authenticated:
        post=get_object_or_404(Article, id=id)
        post.delete()
        return redirect('author_profile')
       
        
        
    else:
        return redirect('login')
        
def getregister(request):
    form=registerUser(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return redirect('login')
    return render(request,"register.html",{"form":form})