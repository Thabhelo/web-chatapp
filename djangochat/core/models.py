from django.db import models

# Create your models here.
class Room(models.Model):
    Name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    
