from django.shortcuts import render,HttpResponse ,redirect
from django.http import HttpResponseRedirect
from .models import Admin ,Work ,Purchase ,Supplier,Billing,Category
from .models import Customer,Delivery,Employee,Feedback,Offer
from .models import Order1,Product,Production,RawMaterial,Recycling,Sales,Stock
from .forms import adminform

# show all table info
def show(request ):
    admin=Admin.objects.all()
    billing=Billing.objects.all()
    category=Category.objects.all()
    customer=Customer.objects.all()
    delivery=Delivery.objects.all()
    employee=Employee.objects.all()
    feedback=Feedback.objects.all()
    offer=Offer.objects.all()
    order1=Order1.objects.all()
    product=Product.objects.all()
    production=Production.objects.all()
    purchase =Purchase.objects.all()
    rawMaterial=RawMaterial.objects.all()
    recycling=Recycling.objects.all()
    sales=Sales.objects.all()
    stock=Stock.objects.all()
    supplier=Supplier.objects.all()
    works =Work.objects.all()
    params ={ 'works':works ,'billing':billing ,'category':category,'customer':customer ,'delivery': delivery ,'employee': employee,'feedback' : feedback ,'offer' : offer,'order1': order1,'product':product,'production':production,'vpurchase':purchase,'rawMaterial':rawMaterial,'recycling':recycling,'sales':sales ,'stock':stock ,'supplier':supplier, 'admin':admin}
    return render (request , "show.html", params)

# navebar
def nav(request):
  return render (request , "nav.html" )

def purchase_add(request):
    if request.method =="POST":
        supplier_id=request.POST.get('supplier')
        vsupplier=Supplier.objects.get(sup_id=supplier_id)
        material_name=request.POST.get('materialname')
        vquantity=request.POST.get('quantity')
        vamount=request.POST.get('amount')
        vpur=Purchase(sup=vsupplier,material=material_name,quantity=vquantity,amount=vamount)
        vpur.save()
        supplier_object=Supplier.objects.all()
        params={'suppliers':supplier_object ,'msg':'massage successfully '}
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'suppliers':Supplier.objects.all()}
    return render (request ,'add_data/purchase_add.html',params)

def workform(request):

    try :
        n=''
        if request.method =="POST":
            # if request.POST.get('workid') and request.POST.get('workname'):
            #     vworksave=Work()
            #     vworksave.work_id=request.POST.get('workid')
            #     vworksave.work_name=request.POST.get('workname')
            #     vworksave.save()
            #     return redirect('show')
            vworkid=request.POST.get('workid')
            vworkname=request.POST.get('workname')
            print(vworkid ,vworkname)
            worksave=Work(work_id =vworkid ,work_name = vworkname)
            worksave.save()
            return redirect('show')
    except :
        return HttpResponse( "bad url")
    params={'n':n}
    return render (request , "workform.html", params)

def customer_add(request):        
    if request.method=="POST":
        vcustomer=Customer(
            customer_fname=request.POST.get('admin_name'),
            customer_lname=request.POST.get('admin_name'),
            contact_number=request.POST.get('admin_name'),
            customer_gender=request.POST.get('admin_name'),
            customer_dob=request.POST.get('admin_name'),
            customer_email=request.POST.get('admin_name'),
            customer_password=request.POST.get('admin_name'),
            address=request.POST.get('admin_name'),
            customer_pincode=request.POST.get('admin_name'))
        vcustomer.save()
        params={'msg':'massage successfully '}
        return render (request , "create.html",params)
    return render (request , "add_data/customer_add.html")
   
def sup_add(request):
    if request.method=="POST":    
        vsup_name=request.POST.get("s_name")
        vcontact_number=request.POST.get("s_con")
        vsup_address=request.POST.get("s_add")
        vsup_email=request.POST.get("s_email")
        vsupplier=Supplier(sup_name=vsup_name,contact_number=vcontact_number,sup_address=vsup_address,sup_email=vsup_email)
        vsupplier.save()

    return render(request , "add_data//sup_add.html")

def admin_add(request):
    if request.method == "POST" :
        vadminname=request.POST.get('admin_name')
        vpassword=request.POST.get('password')
        vadmin=Admin(admin_name=vadminname,password=vpassword)
        vadmin.save()
        params={'msg':'massage successfully '}
        return render (request , "add_data/admin_add.html",params)
    return render (request , "add_data/admin_add.html")

def product_add(request):
    if request.method=="POST":
        fvcategory=request.POST.get("")
        vcategory=Category.objects.get(category_id=fvcategory)
        vproduct_name=request.POST.get("")
        vmaterial=request.POST.get("")
        vimage=request.POST.get("") 
        vproduct_price=request.POST.get("")
        vproduct_weight=request.POST.get("")
        vproduct_quantity=request.POST.get("")
        vproduct_color=request.POST.get("")
        vproduct=Product(category=vcategory,product_name=vproduct_name,material=vmaterial,image=vimage,product_price=vproduct_price,product_weight=vproduct_weight,product_quantity=vproduct_quantity,product_color=vproduct_color)
        vproduct.save()
        params={'category_object':Category.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/order_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'category_object':Category.objects.all()}
    return render (request ,'add_data/purchase_adsd.html',params)    

def production_add(request):
    if request.method=="POST":
        vproduction_id=request.POST.get("")
        fproduct=request.POST.get("")
        vproduct=Product.objects.get(product_id=fproduct)
        vquantity=request.POST.get("")
        vproduction_cost=request.POST.get("")
        vproduction_date=request.POST.get("")
        vproduction=Production(production_id=vproduction_id,product=vproduct,quantity=vquantity,production_cost=vproduction_cost,production_date=vproduction_date)
        vproduction.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/order_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'product_object':Product.objects.all()}
    return render (request ,'add_data/purchase_add.html',params)    

def employee_add(request):
    if request.method=="POST":
        vemp_id=request.POST.get("")
        fvwork=request.POST.get("")
        vwork=Work.objects.get(work=fvwork)
        vemp_name=request.POST.get("")
        vemp_dob=request.POST.get("")
        vcontact_number=request.POST.get("")
        vemp_salary=request.POST.get("")
        vwork_experience=request.POST.get("")
        vemp_joindate=request.POST.get("")
        vemp_leavedate=request.POST.get("")
        vqualification=request.POST.get("")
        vemployee=Employee(emp_id=vemp_id,work=vwork,emp_name=vemp_name,emp_dob=vemp_dob,contact_number=vcontact_number,emp_salary=vemp_salary,work_experience=vwork_experience,emp_joindate=vemp_joindate,emp_leavedate=vemp_leavedate,qualification=vqualification)
        vemployee.save()
        params={'work_object':Work.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/order_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'work_object':Work.objects.all()}
    return render (request ,'add_data/purchase_adsd.html',params)    
    
def order_add(request):
    if request.method=="POST":
        vorder_id=request.POST.get("")
        fvcustomer=request.POST.get("")
        vcustomer=Customer.objects.get(customer_id=fvcustomer)
        vorder_date=request.POST.get("")
        fvproduct=Product.objects.get(product_id=fvproduct)
        vproduct=request.POST.get("")
        vorder_quantity=request.POST.get("")
        vpayment=request.POST.get("")
        vorder1=Order1(order_id=vorder_id,customer=vcustomer,order_date=vorder_date,product=vproduct,order_quantity=vorder_quantity,payment=vpayment)
        vorder1.save()
        customer_object=Customer.objects.all()
        product_object=Product.objects.all()
        params={'customer_object':customer_object ,'product_object':Product.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/order_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all()}
    return render (request ,'add_data/purchase_adsd.html',params)

def delete_admin(request,admin_id):
    
    deletestaff=Admin.objects.get(admin_id=admin_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("show")

def delete_billing(request,bill_id):    
    deletestaff=Billing.objects.get(bill_id=bill_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("show")

def delete_delivery(request , d_id):
    deletestaff=Delivery.objects.get(d_id=d_id)
    deletestaff.delete()
    ans=Admin.objects.all()
    return redirect("show")

def admindasheboard(request ):
    return render (request , "admindasheboard.html")

def adminshow(request)
    admin=Admin.objects.all()
    params ={'admin':admin}
    return render (request , "adminshow.html",params)

def billingshow(request)
    billing=Billing.objects.all()
    params ={'billing':billing}
    return render (request , "billshow.html",params)

def categoryhow(request)
    category=Category.objects.all()
    params ={'category':category}
    return render (request , "categoryshow.html",params)

def customershow(request)
    customer=Customer.objects.all()
    params ={'customer':customer}
    return render (request , "customershow.html",params)

def deliveryshow(request)
    delivery=Delivery.objects.all()
    params ={'delivery':delivery}
    return render (request , "deliveryshow.html",params)

def employeeshow(request)
    employee=Employee.objects.all()
    params ={'employee':employee}
    return render (request , "employeeshow.html",params)

def order1show(request)
    order1=Order1.objects.all()
    params ={'order1':order1}
    return render (request , "ordershow.html",params)

def productshow(request)
    product=Product.objects.all()
    params ={'product':product}
    return render (request , "productshow.html",params)

def productionshow(request)
    production=Production.objects.all()
    params ={'production':production}
    return render (request , "productionshow.html",params)

def stockshow(request)
    stock=Stock.objects.all()
    params ={'stock':stock}
    return render (request , "stockshow.html",params)

def salesshow(request)
    sales=Sales.objects.all()
    params ={'sales':sales}
    return render (request , "saleshow.html",params)

def suppliershow(request)
    supplier=Supplier.objects.all()
    params ={'supplier':supplier}
    return render (request , "suppliershow.html",params)

def workshow(request)
    works =Work.objects.all()
    params ={'works':works}
    return render (request , "workshow.html",params)

def purchaseshow(request)
    vpurchase =Purchase.objects.all()
    params ={'purchase':purchase}
    return render (request , "purchaseshow.html",params)

def rawmaterialshow(request)
    rawMaterial=RawMaterial.objects.all()
    params ={'rawmaterial':rawMaterial}
    return render (request , "rawmaterialshow.html",params)

def recyclingshow(request)
    recycling=Recycling.objects.all()
    params ={'recycling':recycling}
    return render (request , "recyclingshow.html",params)

def feedbackshow(request)
    feedback=Feedback.objects.all()
    params ={'feedback':feedback}
    return render (request , "feedbackshow.html",params)

def offershow(request)
    offer=Offer.objects.all()
    params ={'offer':offer}
    return render (request , "offershow.html",params)

    # return render(request,'delete.html',{'Enrolled':ans})

    # return render (request , "delete.html" ,{'ans' : ans})
#  add this in your html file
#      <p class ="table_cell">
#      <a href="/editcust/{{i.cust_id}}">
#      <span class="icon"><i class="fas fa-edit"></i></span>
#      </a>
                              
# //update query example 
# def auditionupdate(request,audition_id):
#     if request.session.has_key('adminn'):
#         pass
#     else:
#         return redirect('/adminlogin/')
    
#     ff=Audition.objects.all()
#     ff=Audition.objects.get(audition_id=audition_id)
#     ff.audition_type=request.POST['audition_type']
#     ff.cand_fname=request.POST['cand_fname']
#     ff.cand_height=request.POST['cand_height']
#     ff.cand_weight=request.POST['cand_weight']
#     ff.cand_qual=request.POST['cand_qual']
#     ff.mediafile=request.POST['mediafile']
    
#     ff.save()
