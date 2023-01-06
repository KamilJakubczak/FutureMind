from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    height = models.IntegerField()
    width = models.IntegerField()
