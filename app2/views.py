from django.shortcuts import render


# Create your views here.
def home(request):
     return render(request, 'homeapp2.html')


def about(request):
    return render(request, 'aboutapp2.html')