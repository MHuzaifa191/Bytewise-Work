from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Meetup
from .forms import RegForm

# Create your views here.

meetups = Meetup.objects.all()

def index(requests):
    return render(requests, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })

def meetup_item_details(requests, meetup_slug):
    if requests.method == "GET":
        registration_form = RegForm()
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
    else:
        registration_form = RegForm(requests.POST)
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if registration_form.is_valid():
            participant = registration_form.save()
            selected_meetup.participants.add(participant)
            redirect('/success/')
    return render(requests, 'meetups/meetup_item_details.html', {
            'meetup_details': selected_meetup,
            'form': registration_form
    })


def confirm_registration(requests):
    return render(requests, 'meetups/registration_confirmation.html')