from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user     = models.IntegerField()
    name        = models.CharField(max_length=200)
    email       = models.EmailField(max_length=250)
    password    = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username