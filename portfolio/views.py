from django.shortcuts import render, redirect
from django.http import HttpResponse

context = [
	{
	'name':'Andre',
	'age':'27'
	}
]

def index(request):
	data = {
		'data': context
	}
	return render(request, 'portfolio/portfolio.html', data)

def about(request):
	return render(request, 'portfolio/about.html')

def blog(request):
	return render(request, 'portfolio/blog.html')
