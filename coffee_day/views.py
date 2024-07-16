from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib import messages
from datetime import datetime
# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


#landing page
def index(request):
    return render(request, 'index.html')

#display all items
def explore(request):
    return render(request, 'explore.html')

#loginpage
def login(request):
    return render(request, 'login.html')

#display all items to select
def product_list(request):
	products = Product.objects.all()
	return render(request, 'index1.html', {'products': products})

#cart
def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

#function to add cart
def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('admin_update:view_cart')

#function to remove cart
def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('admin_update:view_cart')

def submit_order(request):
    if request.method == 'POST':
        products = request.POST.getlist('products')
        quantities = request.POST.getlist('quantities')
        user = request.user
        current_datetime = datetime.now()
        for product, quantity in zip(products, quantities):
            OrderedItem.objects.create(
                product_name=product,
                quantity=int(quantity),
                user=user,
                date_added=current_datetime
            )
        # Optionally, clear the cart after submitting the order
        CartItem.objects.filter(user=user).delete()
        return redirect('admin_update:order_confirmation')  # Redirect to a confirmation page
    return redirect('cart')  # Redirect back to cart if not a POST request

#checkout
def order_confirmation(request):
    return render(request, 'order_confirmation.html')