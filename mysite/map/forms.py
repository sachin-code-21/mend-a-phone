from django.forms import ModelForm

from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer 
        exclude = ['date_of_request','customer_text']


