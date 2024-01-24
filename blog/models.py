from django.db import models

# Create your models here.
class Blog(models.Model):

    titre = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()