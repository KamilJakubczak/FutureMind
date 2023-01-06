from django.db import models
from django.core.validators import MinValueValidator

# TODO Sclaing before saving
class Image(models.Model):
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploaded/images')
    height = models.IntegerField(validators=[MinValueValidator(1, 'Image height cannot be smaller than 1')])
    width = models.IntegerField(validators=[MinValueValidator(1, 'Image width cannot be smaller than 1')])
