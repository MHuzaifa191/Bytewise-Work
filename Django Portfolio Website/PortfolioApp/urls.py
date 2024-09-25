from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='indexApp'),  # Root URL points to the users view
]