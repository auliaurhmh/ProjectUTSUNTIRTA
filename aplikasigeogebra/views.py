from django.shortcuts import render

# Create your views here.
def indexaplikasigeogebra(request):
    return render(request, 'aplikasigeogebra.html')