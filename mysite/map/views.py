from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .forms import CustomerForm
from .models import Customer

class IndexView(generic.ListView):    
    model = Customer
    template_name = 'map/index.html'


def customerRequest(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.customer_text = 'Request_number'
            post.date_of_request = timezone.now()
            post.save()            
    else:
        form = CustomerForm()
    return render(request, 'map/customer_request.html', {'form': form})
   


