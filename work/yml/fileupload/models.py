from django.db import models


# Create your models here.
class FilePath(models.Model):
    filename=models.CharField(max_length=50)
    filepath=models.CharField(max_length=50)
    