from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Details(models.Model):
	sap = models.CharField(primary_key=True,max_length=20)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	address = models.CharField(max_length=2000)
	source = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	bday=models.DateField()
	year=models.CharField(max_length=10)
	department=models.CharField(max_length=15)
	division=models.CharField(max_length=1)
	time=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=100)
	is_submitted=models.BooleanField(default=False)
	rail_class=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)


	
	def __str__(self):
		return self.name



class Pending(models.Model):
	
	sapid = models.OneToOneField(Details, on_delete=models.CASCADE,primary_key=True)
		


