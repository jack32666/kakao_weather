from django.db import models

# Create your models here.
class weather_DB(models.Model) :
    content = models.CharField(max_length=255)

