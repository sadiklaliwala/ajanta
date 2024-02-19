from unicodedata import category
from django.shortcuts import render

from adminsite.models import Product

def home(request):
 
 #get all products with Category id 1
 el=Product.objects.filter(category_id=1)
 sa=Product.objects.filter(category_id=2)
 pl=Product.objects.filter(category_id=3)
 bt=Product.objects.filter(category_id=5)
 fan=Product.objects.filter(category_id=6)
 params={'el':el,'sa':sa,'pl':pl,'bt':bt,'fan':fan}
 return render(request, 'app/home.html' ,params)

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
