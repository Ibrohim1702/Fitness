from django.db import models

# Create your models here.


class Subscribe(models.Model):
    email = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.email}"

class Contact(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    message = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name