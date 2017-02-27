# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from Flights.models import flight
#Request arg
def home(request):
	return render_to_response('index.html')
