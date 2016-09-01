from django.db import models

from django.db import models
from django.utils import timezone

class Customer(models.Model):
    customer_text = models.CharField(max_length = 200)
    customer_name = models.CharField(max_length = 200)
    customer_email = models.CharField(max_length = 200)
    pickup_address = models.CharField(max_length = 2000)
    pincode = models.IntegerField()
    phone_brand = models.CharField(max_length = 200)
    phone_model = models.CharField(max_length = 200)
    phone_fault = models.CharField(max_length = 200)
    alternate_contact_number = models.IntegerField()
    optional_message = models.CharField(max_length = 2000)
    date_of_request = models.DateTimeField('Date of servece request')    
    def __str__(self):
        return self.customer_text
    

    
