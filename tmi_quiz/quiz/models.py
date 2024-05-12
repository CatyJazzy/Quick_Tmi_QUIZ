from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 30)
    comment = models.TextField('하고 싶은 말')

    def __str__(self):
        return self.name

