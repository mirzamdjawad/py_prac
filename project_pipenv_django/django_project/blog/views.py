from django.shortcuts import render
from django.http import HttpResponse
from . models import Post

# Create your views here.






#def home(request):	
#	context = {
#		'posts': Posts.object.all()
#	}
#	return render(request, 'blog/home.html', context)

def home(request):
	return render(request, 'blog/home.html', {'title' :'Home Page'} )

def about(request):
	return render(request, 'blog/about.html', {'title' :'About'} )

def contactus(request):
	return render(request, 'blog/contactus.html', {'title' :'Contact US'})

