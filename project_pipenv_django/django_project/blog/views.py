from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
 	{
		'author':'John',
		'title':'post 1',
		'content':'contents for blog post1',
		'date_posted':'feb 9, 2022'	
 	}

	{
		'author':'John1',
		'title':'post 2',
		'content':'contents for blog post2',
		'date_posted':'feb 10, 2022'	
 	}	

]





def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title' :'About'} )

def contactus(request):
	return render(request, 'blog/contactus.html', {'title' :'Contact US'})

