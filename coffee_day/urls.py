from django.urls import path
from coffee_day.views import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout

urlpatterns = [
    path('index/', index, name='index'),
    path('explore/', explore, name="explore"),

    path("register/", register_view,name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view,name="logout"),

    path('products_list/', product_list, name='products_list'),
	# path('home/', views.home, name='home'),
	path('cart/', view_cart, name='view_cart'),
	path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('submit_order/', submit_order, name='submit_order'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
]



