from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<h1>Jawad Home Page Django!!!</h1>')

def about(request):
	return HttpResponse('<h1> About Page Django!!!</h1>')

def contactus(request):
	return HttpResponse('<h1> Contact Us Page Django!!!</h1>')

