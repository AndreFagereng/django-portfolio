from django.urls import path
from . import views

urlpatterns =[
	path('', views.index, name='portfolio-home'),
	path('about/',views.about, name='portfolio-about'),
	path('blog/', views.blog, name='portfolio-blog')
]