from django.urls import path
from .views import *

urlpatterns = [
    path('', redirect_to_admin, name='home'),
    path('index/', index, name='index'),
    path('save-analysis/', save_analysis_ajax, name='save_analysis_ajax'),
    path('pest_list/<int:pk>/', pest_list, name='pest_list'),
    path('risk/<int:pk>/', risk, name='risk'),
]