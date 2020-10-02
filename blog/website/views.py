from django.shortcuts import render
from .models import Post

def hello_blog(request):
	lista = ['django', 'python', 'html', 'gabriel']
	list_posts = Post.objects.filter(deleted=False)
	data = {
		'name': 'Curso de Django 3', 
		'listatec': lista, 
		'posts': list_posts,
	}

	return render(request, 'index.html', data)
