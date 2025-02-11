from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class MyUser(AbstractUser):
    STATUS = (
        ('regular', 'regular'),
        ('entitled', 'entitled'),
        ('moderator', 'moderator'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField('description', max_length=700, default='', blank=True)
    def __str__(self):
        return self.username
