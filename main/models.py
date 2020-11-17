from django.db import models


# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=1024)
    image_url = models.CharField(max_length=512)

    def __str__(self):
        return self.name
