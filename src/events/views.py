from django.shortcuts import render
from .models import Event
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template.loader import render_to_string
from .forms import EventForm

# Create your views here.
def events_list(request):
    events = Event.objects.all().order_by("-datetime_event")
    return render(request, 'events/list.html', {'events':events})

def event_detail(request, event_id):
    event_detail = get_object_or_404(Event, pk=event_id)
    form = EventForm()
    return render(request, 'events/detail.html', {'event':event_detail, 'event_form':form})
