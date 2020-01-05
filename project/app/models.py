from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.TextField(primary_key=True)
    title = models.TextField()
    descript = models.TextField()
    email = models.CharField(max_length=64)
    img = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name} ({self.email}) - {self.title}'

class MailList(models.Model):
    fullname = models.TextField(primary_key=True)
    email = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.fullname} ({self.email})'
