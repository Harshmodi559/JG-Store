from django.db import models

# Create your models here.
import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    mobile_number=models.IntegerField()
    date=models.DateField(auto_now=True,blank=True)
    note=models.TextField()
    amount=models.IntegerField()



    

