
from django.contrib.auth.models import User
from django.db import models


class Banana(models.Model):
    users = models.ManyToManyField(User, blank=True)
