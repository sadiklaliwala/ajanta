from email.contentmanager import raw_data_manager
from statistics import quantiles
from urllib import request
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

def billing_add(request):
    if request.method=='POST':
        vcustomer=request.POST.get("customer")
        fvcustomer=request.POST.get(customer=vcustomer)
        vorder=request.POST.get("order")
        vshipping_charges=request.POST.get("shippingcharges")
        vorder_date=request.POST.get("orderdate")
        vtotal=request.POST.get("totalamount")
        vbilling=Billing(customer=fvcustomer,order=vorder,shipping_charges=vshipping_charges,order_date=vorder_date,total=vtotal)
        vbilling.save()
        return render(request , "add_data/billing.html")
    params={'customerss':Customer.objects.all()}
    return render (request ,'add_data/billing.html',params)    

def admin_add(request):
    if request.method == "POST" :
        vadminname=request.POST.get('admin_name')
        vpassword=request.POST.get('password')
        vadmin=Admin(admin_name=vadminname,password=vpassword)
        vadmin.save()
        params={'msg':'massage successfully '}
        return render (request , "add_data/admin_add.html",params)
    return render (request , "add_data/admin_add.html")

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

def delivery_add(request):
    if request.method=="POST":
        vcustomername=request.POST.get('customername')
        fvcustomer=Customer.objects.get(customer=vcustomername)
        vaddress =request.POST.get("address")
        vproduct =request.POST.get("product")
        vd_date =request.POST.get("deliverydate")
        vemp =request.POST.get("employee")
        vquantity =request.POST.get("quantity")
        vdelivery=Delivery(customer=fvcustomer,address=vaddress,product=vproduct,d_date=vd_date,emp=vemp,quantity=vquantity)
        vdelivery.save()
        return render (request , "add_data/delivery_add.html")
    params={'customer':Customer.objects.all()}
    return render (request , "add_data/delivery_add.html",params)

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
            # vworkid=request.POST.get('workid')
            vworkname=request.POST.get('workname')
            # print(vworkid ,vworkname)
            worksave=Work(work_name = vworkname)
            worksave.save()
            return redirect('show')
    except :
        return HttpResponse( "bad url")
    params={'n':n}
    return render (request , "workform.html", params)

def sup_add(request):
    if request.method=="POST":    
        vsup_name=request.POST.get("s_name")
        vcontact_number=request.POST.get("s_con")
        vsup_address=request.POST.get("s_add")
        vsup_email=request.POST.get("s_email")
        vsupplier=Supplier(sup_name=vsup_name,contact_number=vcontact_number,sup_address=vsup_address,sup_email=vsup_email)
        vsupplier.save()

    return render(request , "add_data//sup_add.html")

def category_add(request):
    if request.method=="POST":
        vcategory_name=request.POST.get("categoryname")
        vcategory=Category(category_name=vcategory_name)
        vcategory.save()
        return render (request , "add_data/category_add.html")
    return render (request , "add_data/category_add.html")

def product_add(request):
    if request.method=="POST":
        fvcategory=request.POST.get("category")
        vcategory=Category.objects.get(category_id=fvcategory)
        vproduct_name=request.POST.get("productname")
        vmaterial=request.POST.get("material")
        vimage=request.POST.get("image") 
        vproduct_price=request.POST.get("productprice")
        vproduct_weight=request.POST.get("productweight")
        vproduct_quantity=request.POST.get("productquantity")
        vproduct_color=request.POST.get("productcolor")
        vproduct=Product(category=vcategory,product_name=vproduct_name,material=vmaterial,image=vimage,product_price=vproduct_price,product_weight=vproduct_weight,product_quantity=vproduct_quantity,product_color=vproduct_color)
        vproduct.save()
        params={'category_object':Category.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/product_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'category_object':Category.objects.all()}
    return render (request ,'add_data/product_add.html',params)    

def recycling_add(request):
    if request.method=="POST":
        vr_date=request.POST.get("recyclingdate")
        vquantity=request.POST.get("quantity")
        recycling=Recycling(r_date=vr_date,quantity=vquantity)
        recycling.save()
        return render(request , "add_data/recycling_add.html")  
    return render(request , "add_data/recycling_add.html")  

def production_add(request):
    if request.method=="POST":
        fproduct=request.POST.get("product")
        vproduct=Product.objects.get(product_id=fproduct)
        vquantity=request.POST.get("quantity")
        vproduction_cost=request.POST.get("productioncost")
        vproduction_date=request.POST.get("productiondate")
        vproduction=Production(product=vproduct,quantity=vquantity,production_cost=vproduction_cost,production_date=vproduction_date)
        vproduction.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/production_add.html")
    params={'product_object':Product.objects.all()}
    return render (request ,'add_data/production_add.html',params)    

def employee_add(request):
    if request.method=="POST":
        fvwork=request.POST.get("work")
        vwork=Work.objects.get(work=fvwork)
        vemp_name=request.POST.get("employeename")
        vemp_dob=request.POST.get("employeedob")
        vcontact_number=request.POST.get("contact")
        vemp_salary=request.POST.get("salary")
        vwork_experience=request.POST.get("experience")
        vemp_joindate=request.POST.get("joiningdate")
        vemp_leavedate=request.POST.get("leavedate")
        vqualification=request.POST.get("qualification")
        vemployee=Employee(work=vwork,emp_name=vemp_name,emp_dob=vemp_dob,contact_number=vcontact_number,emp_salary=vemp_salary,work_experience=vwork_experience,emp_joindate=vemp_joindate,emp_leavedate=vemp_leavedate,qualification=vqualification)
        vemployee.save()
        params={'work_object':Work.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/employee.html")
    params={'work_object':Work.objects.all()}
    return render (request ,'add_data/employee.html',params)    

def rawmaterial_add(request):
    if request.method=="POST":
        vsup=request.POST.get("supplier")
        fvsup=Supplier.objects.get(sup_id=vsup)
        vraw_name=request.POST.get("rawmaterialname")
        vraw_quantity=request.POST.get("quantity")
        rawmaterial=RawMaterial(sup=fvsup,raw_name=vraw_name,raw_quantity=vraw_quantity)
        rawmaterial.save()
        return render(request , "add_data/rawmaterial_add.html")
    params={'supplier_object': Supplier.objects.all}
    return render(request , "add_data/rawmaterial_add.html",params)

def order_add(request):
    if request.method=="POST":
        fvcustomer=request.POST.get("customer")
        vcustomer=Customer.objects.get(customer_id=fvcustomer)
        vorder_date=request.POST.get("orderdate")
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vorder_quantity=request.POST.get("o_quantity")
        vpayment=request.POST.get("payment")
        vorder1=Order1(customer=vcustomer,order_date=vorder_date,product=fvproduct,order_quantity=vorder_quantity,payment=vpayment)
        vorder1.save()
        customer_object=Customer.objects.all()
        product_object=Product.objects.all()
        params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/order_add.html")
        # return render (request , 'purchaseform.html',params)
        # from here all supplier name are coming 
    params={'customer_object':Customer.objects.all(),'product_object':Product.objects.all()}
    return render (request ,'add_data/purchase_adsd.html',params)

def feedback_add(request):
    if request.method == "POST" : 
        vf_date=request.POST.get("f_date") 
        vfeedback=request.POST.get("feedback") 
        vcustomer=request.POST.get("customer")
        fvcustomer=Customer.objects.get(customer_id=vcustomer)
        feedback=Feedback(f_date=vf_date,feedback=vfeedback,customer=fvcustomer)
        feedback.save()
        params={'msg':'massage successfully ','customer_object':Customer.objects.all()}
        return render (request , "add_data/feedback_add.html",params)
    params={'msg':'massage successfully ','customer_object':Customer.objects.all()}
    return render (request , "add_data/feedback_add.html")

def offer_add(request):
    if request.method == "POST" :
        vstart_date=request.POST.get("sdate")
        vend_date=request.POST.get("edate")
        vdescription=request.POST.get("description")
        offer=Offer(start_date=vstart_date,end_date=vend_date,description=vdescription)
        offer.save()
        params={'msg':'massage successfully '}
        return render (request , "add_data/offer_add.html",params)
    return render (request , "add_data/offer_add.html")

def sales_add(request):
    if request.method=="POST":
        vsales_date=request.POST.get("salesdate")
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vquantity=request.POST.get("quantity")
        vsales=Sales(sales_date=vsales_date,product=fvproduct,quantity=vquantity)
        vsales.save()
        params={'product_object':Product.objects.all(),'msg':'massage successfully '}
        return render(request , "add_data/sales.html")
    params={'product_object':Product.objects.all()}
    return render (request ,'add_data/sales.html',params)

def stock_add(request):
    if request.method =="POST":
        vproduct=request.POST.get("product")
        fvproduct=Product.objects.get(product_id=vproduct)
        vr_id=request.POST.get("rawmaterial")
        fvr_id=RawMaterial.objects.get(raw_id=vr_id)
        vquantity=request.POST.get("quantity")
        vmaterial_quantity=request.POST.get("materialquantity")
        stock=Stock(product=fvproduct,r_id=fvr_id,quantity=vquantity,material_quantity=vmaterial_quantity)
        params={'rawMaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all()}
        return render(request , "add_data/sales.html")
    params={'rawMaterial_object':RawMaterial.objects.all(),'product_object':Product.objects.all()}
    return render (request ,'add_data/sales.html',params)


#update
def workform_update(request,pk):
    if request.method=="POST":
        # s=Work.objects.get(work_id=pk)
        vworkname=request.POST.get("workname")
        worksave=Work(work_id=pk,work_name = vworkname)
        worksave.save()
        return redirect ("workshow")
    params={'work_object':Work.objects.get(work_id=pk)}
    return render (request , "update_data/workform_update.html",params)






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

def adminbase(request ):
    return render (request , "basepage.html")

def adminshow(request):
    admin=Admin.objects.all()
    params ={'admin':admin}
    return render (request , "show_data/adminshow.html",params)

def billingshow(request):
    billing=Billing.objects.all()
    params ={'billing':billing}
    return render (request , "show_data/billshow.html",params)

def categoryhow(request):
    category=Category.objects.all()
    params ={'category':category}
    return render (request , "show_data/categoryshow.html",params)

def customershow(request):
    customer=Customer.objects.all()
    params ={'customer':customer}
    return render (request , "show_data/customershow.html",params)

def deliveryshow(request):
    delivery=Delivery.objects.all()
    params ={'delivery':delivery}
    return render (request , "show_data/deliveryshow.html",params)

def employeeshow(request):
    employee=Employee.objects.all()
    params ={'employee':employee}
    return render (request , "show_data/employeeshow.html",params)

def order1show(request):
    order1=Order1.objects.all()
    params ={'order1':order1}
    return render (request , "show_data/ordershow.html",params)

def productshow(request):
    product=Product.objects.all()
    params ={'product':product}
    return render (request , "show_data/productshow.html",params)

def productionshow(request):
    production=Production.objects.all()
    params ={'production':production}
    return render (request , "show_data/productionshow.html",params)
        
def stockshow(request):
    stock=Stock.objects.all()
    params ={'stock':stock}
    return render (request , "show_data/stockshow.html",params)

def salesshow(request):
    sales=Sales.objects.all()
    params ={'sales':sales}
    return render (request , "show_data/saleshow.html",params)

def suppliershow(request):
    supplier=Supplier.objects.all()
    params ={'supplier':supplier}
    return render (request , "show_data/suppliershow.html",params)

def workshow(request):
    works =Work.objects.all()
    params ={'works':works}
    return render (request , "show_data/workshow.html",params)

def purchaseshow(request):
    vpurchase =Purchase.objects.all()
    params ={'purchase':Purchase.objects.all()}
    return render (request , "show_data/purchaseshow.html",params)

def rawmaterialshow(request):
    rawMaterial=RawMaterial.objects.all()
    params ={'rawmaterial':rawMaterial}
    return render (request , "show_data/rawmaterialshow.html",params)

def recyclingshow(request):
    recycling=Recycling.objects.all()
    params ={'recycling':recycling}
    return render (request , "show_data/recyclingshow.html",params)

def feedbackshow(request):
    feedback=Feedback.objects.all()
    params ={'feedback':feedback}
    return render (request , "show_data/feedbackshow.html",params)

def offershow(request):
    offer=Offer.objects.all()
    params ={'offer':offer}
    return render (request , "show_data/offershow.html",params)



    # return render(request,'delete.html',{'Enrolled':ans})

    # return render (request , "delete.html" ,{'ans' : ans})
 






# add this in your html file
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
