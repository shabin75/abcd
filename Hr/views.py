from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    d = {'head': '12334', 'des': 'gfjshgfjsgjfjfgjgfjj'}
    return render(request, 'index.html', d)


def about(request):
    return render(request, 'about.html')
