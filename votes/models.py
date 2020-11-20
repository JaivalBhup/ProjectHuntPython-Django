from django.db import models
from django.contrib.auth.models import User
from products.models import Project
# Create your models here.


class Votes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)



