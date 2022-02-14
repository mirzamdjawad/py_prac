from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.






def home(request):	
	return render(request, 'blog/home.html', {'title' :'Home'})

def about(request):
	return render(request, 'blog/about.html', {'title' :'About'} )

def contactus(request):
	return render(request, 'blog/contactus.html', {'title' :'Contact US'})

