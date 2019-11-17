from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render (request,"todo.htm", {
        'all_items':all_todo_items
    })

def addTodo(request):
   c = request.POST['content']
   new_item = TodoItem(content=c)
   new_item.save()
   return redirect('/')

def deleteTodo(request,todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect('/')




