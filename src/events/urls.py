from django.urls import path, include

from .views import (
        events_list,
        event_detail,
        )

app_name = 'events'

urlpatterns = [
    path('', events_list, name='home'),
    path('list/<int:event_id>', event_detail, name='details'),
]
