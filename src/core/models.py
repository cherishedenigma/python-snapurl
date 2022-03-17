import imp
import re
from django.db import models
from django.shortcuts import redirect
from django.conf import settings
from django.template import Origin
from core.validators import uri_validator
    
#Input Model. Accepts a valid URL Resource as Origin
class Post(models.Model):
    origin = models.CharField(max_length=200, validators=[uri_validator])


#Output Model. 
class SnapUrl(models.Model):
    id = models.AutoField(primary_key=True)
    hash= models.CharField(max_length=10)
    origin= models.CharField(max_length=200)
    url= models.CharField(max_length=200)

    def __str__(self):
        return f'{settings.APP_KEYS["Domain"]}{self.hash} for {self.origin}'


