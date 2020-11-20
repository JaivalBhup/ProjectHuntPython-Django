from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    req_langs = models.CharField(max_length=100)
    sp_framework = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    total_votes = models.IntegerField(default=0)
    icon = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

