from django.db import models

# Create your models here.
class director_login(models.Model):
	duser = models.CharField(max_length=100)
	dpass = models.CharField(max_length=100)