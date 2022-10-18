from django.shortcuts import render

# Create your views here.
def indexpendahuluan(request):
    return render(request, 'pendahuluan.html')