from django.db import models

# Create your models here.
class UserData(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName