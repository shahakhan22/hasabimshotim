from django.shortcuts import render
from .models import Partner

# Create your views here.
def partners_list(request):
    partners = Partner.objects.all()
    return render(request, 'partners/list.html', {'partners':partners})
