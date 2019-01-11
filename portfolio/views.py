from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import gitapi as api

def index(request):
	
	try:
		repository_data = api.get_response('https://api.github.com/users/AndreFagereng/repos')
		data = api.list_view(repository_data)
		
		data = {
		'data': data
		}
		
		return render(request, 'portfolio/portfolio.html', data)	
	except:
		pass
	
	
	

def about(request):
	return render(request, 'portfolio/about.html')

def blog(request):
	return render(request, 'portfolio/blog.html')
