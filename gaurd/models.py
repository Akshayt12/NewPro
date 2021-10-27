from django.db import models

# Create your models here.
class gaurds(models.Model):
	guser = models.CharField(max_length=100)
	gfname = models.CharField(max_length=100)
	glname = models.CharField(max_length=100)
	gpass = models.CharField(max_length=100)
	
class guest_enteries(models.Model):
	intime = models.CharField(max_length=100)
	extime = models.CharField(max_length=100)
	guest_name = models.CharField(max_length=100)
	purpose = models.CharField(max_length=100)
	comefrom = models.CharField(max_length=100)