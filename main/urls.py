from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_to_admin, name='home'),
    path('index/', index, name='index')
]
