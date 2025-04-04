from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import *


def redirect_to_admin(request):
    return redirect('/admin/login/?next=/admin/')

@login_required
def index(request):
    context = {
        'area': Area.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'index.html',context)
