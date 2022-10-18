from django.shortcuts import render

# Create your views here.
def indexglosarium(request):
    return render(request, 'glosarium.html')