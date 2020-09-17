from django.shortcuts import render

def hello_blog(request):
	lista = ['django', 'python', 'html', 'gabriel']
	data = {'name': 'Curso de Django 3', 'listatec': lista}
	return render(request, 'index.html', data)
