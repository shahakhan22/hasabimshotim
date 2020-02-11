"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from carts.views import cart_home

from .views import homepage, contact, about, login_page, register_page
# from products.views import (
#         ProductListView,
#         product_list_view,
#         ProductDetailView,
#         ProductDetailSlugView,
#         product_detail_view,
#         ProductFeaturedListView,
#         ProductFeaturedDetailView
#         )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name = "homepage"),
    path('login/', login_page, name = "login_page"),
    path('register/', register_page, name = "register_page"),
    path('contact/', contact, name = "contact"),
    path('about/', about, name="about"),
    path('products/', include("products.urls")),
    path('cart/', cart_home, name='cart'),


    # path('featured/', ProductFeaturedListView.as_view()),
    # path('featured/<pk>/', ProductFeaturedDetailView.as_view()),
    # path('products/<slug>/', ProductDetailSlugView.as_view()),
    # path('products/', ProductListView.as_view()),
    # path('products-fbv/', product_list_view, name='product_list_view'),
    # # path('products/<pk>/', ProductDetailView.as_view()),
    # path('products-fbv/<pk>/', product_detail_view),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
