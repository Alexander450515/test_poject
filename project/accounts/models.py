from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    name = models.CharField('имя', max_length=50)
    birthday = models.DateTimeField('день рождения')
    account = models.ManyToManyField(User)
