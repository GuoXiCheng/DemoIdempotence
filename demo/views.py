import time

from django.shortcuts import render

# Create your views here.
from faker import Faker

from demo.models import User
import uuid


def DemoDelete(request):
    user_list = User.objects.all()
    fake = Faker()
    # User.objects.create(
    #     user_id=uuid.uuid4(), user_name=fake.name(), email=fake.free_email()
    # )
    return render(request, "delete.html", {"user_list": user_list})


def DemoUpdate(request):
    return render(request, "update.html")

def DemoInsert(request):
    return render(request, "insert.html")

def DeleteById(request):
    if request.method == "POST":
        time.sleep(3)
        print("hhh")
        user = User.objects.filter(user_id=request.POST['user_id'])
        print(user)
        if user:
            user.delete()
        user_list = User.objects.all()
        return render(request, "delete.html", {"user_list": user_list})
