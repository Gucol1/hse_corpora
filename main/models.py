from django.db import models

# Create your models here.

class Main(models.Model):
    word = models.TextField(unique=True)
    rank = models.IntegerField()
    frequency = models.IntegerField()
    range = models.IntegerField()
    normalized_freq = models.IntegerField()
    normalized_range = models.IntegerField()

    def __str__(self):
        return self.word