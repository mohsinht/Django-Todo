from django.shortcuts import render
from .models import Todo


# Create your views here.
def index(request):
    all_todo = Todo.objects.all()
    return render(request,'todo/index.html',{"all_todo":all_todo})