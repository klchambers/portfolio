from django.db import models


class HomePage(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField(max_length=254)
    email = models.EmailField()
