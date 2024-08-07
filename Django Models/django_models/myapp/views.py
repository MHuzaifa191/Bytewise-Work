from django.shortcuts import render
from django.views.generic import View
from .models import Person, PersonAddress, City, Interest

class HomeView(View):
    def get(self, request, *args, **kwargs):
        person = Person.objects.get(id=2)
        for interest in person.interests.all():
            print(f"{interest}")
        
        context = {}
        return render(request, 'myapp/home.html', context)