from django.shortcuts import render

# Create your views here.
def indexcover(request):
    return render(request, 'cover.html')