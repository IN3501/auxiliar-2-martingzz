from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def pestaña(request):
	return render(request, 'miapp/pestaña.html')
	
def Docentes(request):
	return render(request, 'miapp/Docentes.html')

def Autos(request):
	return render(request, 'miapp/Autos.html')
