from django.db import models
from django.core.validators import MinValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from utils import resize_image


class Image(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    height = models.IntegerField(validators=[MinValueValidator(1, 'Image height cannot be smaller than 1')])
    width = models.IntegerField(validators=[MinValueValidator(1, 'Image width cannot be smaller than 1')])


# @receiver(pre_save)
# def resize_image_before_save(sender, instance, *args, **kwargs):
#     try:
#         instance.image.file = resize_image(instance.image, instance.width, instance.height)
#     except:
#         pass
