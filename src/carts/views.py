from django.shortcuts import render

from .models import Cart


# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('New Cart created')
#     return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    print(cart_obj.total)
    cart_obj.save()
    print(cart_obj.total)

    return render(request, "carts/home.html", {})
