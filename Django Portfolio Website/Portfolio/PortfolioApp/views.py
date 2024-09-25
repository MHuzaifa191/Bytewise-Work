from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.


def index(request):
    try:
        return render(request, 'PortfolioApp/index.html')
    except TemplateDoesNotExist as e:
        print(e)  # This will help you see what Django is searching for