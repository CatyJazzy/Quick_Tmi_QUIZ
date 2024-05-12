from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comment = models.TextField('하고 싶은 말')
    answers = models.CharField(max_length=25)
    # "1번점수-2번점수- ... -13번점수" 형식으로 저장

    def __str__(self):
        return self.name

