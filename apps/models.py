from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Appetizer(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class Sushi(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class Sashimi(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name


class A_La_Carte(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name


class Rolls(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class Vegetarian_Rolls(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name


class Special_Rolls(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

class WB_Special_Rolls(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(max_length=50)
    def __str__(self):
	    return self.name

#class Platter(models.Model):
#    name = models.CharField(max_length=30)
#    price = models.FloatField()
#	description = models.CharField(max_length=50)
#	
#    def __str__(self):
#        return self.size + " " + self.name	