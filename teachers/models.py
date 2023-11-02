from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    email = models.EmailField()
    number = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='uploads/images/', default='uploads/images/default.jpg')

    def __str__(self):
        return self.name


class Sliders(models.Model):
    text1 = models.CharField(max_length=40, blank=False, null=False)
    text2 = models.CharField(max_length=40, blank=False, null=False)
    image = models.ImageField(upload_to='uploads/sliders/', default='')

    def __str__(self):
        return self.text1
