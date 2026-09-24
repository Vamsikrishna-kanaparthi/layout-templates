from django.db import models

class student(models.Model):
    studentid = models.IntegerField()
    studentname = models.CharField(max_length=40)
    studentfee = models.IntegerField()