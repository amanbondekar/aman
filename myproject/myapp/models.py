from django.db import models

class Person(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Password_confirmation = models.IntegerField()
