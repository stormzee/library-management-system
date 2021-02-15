from django.urls import path

from .views import borrow
urlpatterns = [
    path('', borrow, name='borrow')
]