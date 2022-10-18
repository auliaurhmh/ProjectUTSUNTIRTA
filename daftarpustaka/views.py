from django.shortcuts import render

# Create your views here.
def indexdaftarpustaka(request):
    return render(request, 'daftarpustaka.html')