from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Area, Category, Analysis, Pest
from .forms import NewAnalysisForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.urls import reverse
import json


def redirect_to_admin(request):
    return redirect('/admin/login/?next=/admin/')



@login_required
def index(request):
    context = {
        'area': Area.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'main/index.html', context)

@login_required
def pest_list(request, pk):
    analysis = get_object_or_404(Analysis, id=pk)
    pests = Pest.objects.filter(analysis=analysis)
    return render(request, 'main/pest_list.html', {'pest': pests})

@csrf_exempt
@login_required
def save_analysis_ajax(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            area = request.POST.get('area')
            name = request.POST.get('name')
            body = request.POST.get('body')
            volume = request.POST.get('volume')
            eksports_id = request.POST.get('eksports')
            imports_id = request.POST.get('imports')
            category_id = request.POST.get('category')
            pests = json.loads(request.POST.get('pests'))  # [{'title': 'Aphid'}, {'title': 'Thrips'}, ...]

            analysis = Analysis.objects.create(
                title=title,
                area=area,
                name=name,
                body=body,
                volume=volume,
                eksports_id=eksports_id,
                imports_id=imports_id,
                category_id=category_id,
                author=request.user
            )

            for pest in pests:
                Pest.objects.create(
                    analysis=analysis,
                    title=pest['title']
                )

            return JsonResponse({'success': True, 'redirect_url': reverse('pest_list', args=[analysis.id])})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid method'})