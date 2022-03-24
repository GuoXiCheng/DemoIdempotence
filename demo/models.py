from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(db_column="user_id", max_length=255)
    user_name = models.CharField(db_column="user_name", max_length=255)
    email = models.CharField(db_column="email", max_length=255)

    class Meta:
        db_table = "User"
