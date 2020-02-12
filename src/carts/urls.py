from django.urls import path, include

from .views import (
        cart_home,
        cart_update,
        )

app_name = 'carts'

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
]
