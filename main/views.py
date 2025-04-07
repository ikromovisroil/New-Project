from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Area, Category, Analysis, Pest
from .forms import NewAnalysisForm
import re
from django.shortcuts import get_object_or_404
from bs4 import BeautifulSoup



def redirect_to_admin(request):
    return redirect('/admin/login/?next=/admin/')

@login_required
def index(request):
    if request.method == 'POST':
        form = NewAnalysisForm(request.POST)
        if form.is_valid():
            analysis = form.save(commit=False)
            analysis.author = request.user
            analysis.save()

            from bs4 import BeautifulSoup

            soup = BeautifulSoup(analysis.body or "", 'html.parser')
            ol = soup.find('ol')

            if ol:
                for li in ol.find_all('li', recursive=False):
                    title_tag = li.find('strong')
                    if not title_tag:
                        continue

                    title = title_tag.get_text(strip=True)
                    damage = ''
                    protection = ''

                    for sub_li in li.find_all('li'):
                        text = sub_li.get_text(strip=True)
                        if text.lower().startswith('damage:'):
                            damage = text.split(':', 1)[1].strip()
                        elif text.lower().startswith('protection:'):
                            protection = text.split(':', 1)[1].strip()

                    Pest.objects.create(
                        analysis=analysis,
                        title=title,
                        damage=damage,
                        protection=protection
                    )

            messages.success(request, "Ma'lumotlar va pestlar saqlandi.")
            return redirect(reverse('pest_list', args=[analysis.id]))
        else:
            messages.error(request, "Xatolik: Ma'lumot to'g'ri emas.")
    else:
        form = NewAnalysisForm()

    context = {
        'form': form,
        'area': Area.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'main/index.html', context)


@login_required
def pest_list(request,pk):
    analysis_id = get_object_or_404(Analysis, id=pk)
    context = {
        'pest': Pest.objects.filter(analysis_id=analysis_id, analysis__author=request.user),
    }
    return render(request, 'main/pest_list.html',context)