from django.shortcuts import render

# Create your views here.
from faker import Faker

from demo.models import User
import uuid


def DemoDelete(request):
    user_list = User.objects.all()
    fake = Faker()
    User.objects.create(
        user_id=uuid.uuid4(), user_name=fake.name(), email=fake.free_email()
    )
    return render(request, "demo-delete.html", {"user_list": user_list})
