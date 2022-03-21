from django.shortcuts import render

# Create your views here.

def DemoDelete(request) :
    return render(request, "demo-delete.html")