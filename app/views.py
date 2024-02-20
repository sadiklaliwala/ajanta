from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib import messages
from adminsite.models import Product ,Customer

def home(request):
 
 #get all products with Category id 1
 el=Product.objects.filter(category_id=1)
 sa=Product.objects.filter(category_id=2)
 pl=Product.objects.filter(category_id=3)
 bt=Product.objects.filter(category_id=5)
 fan=Product.objects.filter(category_id=6)
 params={'el':el,'sa':sa,'pl':pl,'bt':bt,'fan':fan}
 return render(request, 'app/home.html' ,params)

def product_detail(request,pk):
 product=Product.objects.get(product_id=pk)
 params={'product':product}
 return render(request, 'app/productdetail.html', params)

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

def mobile(request,data=None):
 if data == None:
  ei=Product.objects.filter(category_id=1)
 elif data== 'fan' or data == 'bottle':
    ei=Product.objects.filter(category_id=2)
 params={'electricItem':ei }
 return render(request, 'app/mobile.html',params)

def login(request):
 if request.method=='POST':
        email=request.POST['email']
        pass1=request.POST['password']

        if Customer.objects.filter(customer_email=email).exists():

            if Customer.objects.filter(customer_password=pass1).exists():

                data = Customer.objects.filter(customer_email=email,customer_password=pass1 )
    
                for data in data:
                    request.session['cid']=data.customer_id
                    return redirect('home')
                else:
                    messages.info(request, 'Invalid Credentials')
                    return redirect('login')
            else:
                messages.info(request,'Invalid Password')
                return redirect('login')
        else:
            messages.info(request,'Invalid Email', extra_tags='info')
            # messages.success(request,'Success from login', extra_tags='success')
            return redirect('login')
 
 return render(request, 'app/login.html')

def customerregistration(request):
    if request.method=="POST":
        vcustomer=Customer(
            customer_fname=request.POST.get('customerfname'),
            customer_lname=request.POST.get('customerlname'),
            contact_number=request.POST.get('number'),
            customer_gender=request.POST.get('gender'),
            customer_dob=request.POST.get('customerdob'),
            customer_email=request.POST.get('emailid'),
            customer_password=request.POST.get('password'),
            address=request.POST.get('address'),
            customer_pincode=request.POST.get('pincode'))
        vcustomer.save()
        params={'customer':Customer.objects.all(),'msg':'massage successfully '}
        return redirect('login')
    params={'customer':Customer.objects.all(),'msg':'massage successfully '}
    return render(request, 'app/customerregistration.html',params)

def checkout(request):
 return render(request, 'app/checkout.html')
