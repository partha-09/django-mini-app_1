from django.db import models

# Create your models here.
class Details(models.Model):
    def __str__(self):
        return self.firstname;
    firstname=models.CharField(max_length=122);
class Registration(models.Model):
    firstname = models.CharField(max_length=122)  # Field for name
    email = models.EmailField(max_length=122)     # Field for email
    phone = models.CharField(max_length=15)