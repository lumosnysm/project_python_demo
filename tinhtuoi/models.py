from django.db import models

class Calculate(models.Model):
    status = models.BooleanField(blank=True, null=True)

class GenDoc(models.Model):
    text = models.CharField(max_length=1000)
