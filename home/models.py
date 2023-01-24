from django.db import models

# Create your models here.

class Count(models.Model):
    like = models.IntegerField()
    dislike = models.IntegerField()
