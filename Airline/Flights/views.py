# Create your views here.
from django.shortcuts import render_to_response

from Flights.models import flight
#Request arg
def home(request):
	return render_to_response('index.html')
