from django.db import models


# Create your models here.

# save user input to a model
class Url(models.Model):
    link = models.CharField(max_length=10000)  # some links are very long
    uuid = models.CharField(max_length=10) # shor link id
