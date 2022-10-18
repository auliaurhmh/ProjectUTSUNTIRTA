from django.shortcuts import render

# Create your views here.
def indexkatapengantar(request):
    return render(request, 'katapengantar.html')