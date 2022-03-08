from django.db import models

# Create your models here.

class Resource(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    html_url = models.URLField(max_length=200)

    def __str__(self):
    	return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name