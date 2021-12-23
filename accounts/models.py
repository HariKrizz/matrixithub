from django.db import models
from django.db.models.deletion import CASCADE


class Account(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    uname = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    passwd= models.CharField(max_length=50)

    def __str__(self):
        return self.uname