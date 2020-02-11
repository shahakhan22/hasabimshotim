from django.urls import path

from .views import (
        ProductListView,
        ProductDetailSlugView,
        )

urlpatterns = [
        path('<slug>/', ProductDetailSlugView.as_view()),
        path('', ProductListView.as_view(), name='products'),
]
