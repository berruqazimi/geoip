from django.urls import path
from .views import home

urlpatterns = [
    # ...
    path('search/', home, name='home'),
]
