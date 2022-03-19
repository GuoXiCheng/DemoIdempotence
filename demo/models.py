from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(db_column="user_name", max_length=255)
    age = models.IntegerField(db_column="age")

    class Meta:
        db_table = "User"
