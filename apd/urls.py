"""
URL configuration for apd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from adminsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
      path('admindasheboard/', views.admindasheboard,name="admindasheboard"),
      
    # path('',include('adminsite.urls'))
     #all data show 
      path('show/',views.show, name ="show"),
      path('adminbase' ,views.adminbase , name= "adminbase"),
      path('bill_show',views.billingshow, name="billingshow"),
      path('admin_show', views.adminshow, name="adminshow"),
      path('category_show', views.categoryhow, name="categoryhow"),
      path('customer_show', views.customershow, name="customershow"),
      path('delivery_show', views.deliveryshow, name="deliveryshow"),
      path('employee_show', views.employeeshow, name="employeeshow"),
      path('feedback_show', views.feedbackshow, name="feedbackshow"),
      path('offer_show', views.offershow, name="offershow"),   
      path('production_show', views.productionshow, name="productionshow"),
      path('product_show', views.productshow, name="productshow"),
      path('purchase_show', views.purchaseshow, name="purchaseshow"),
      path('raw_show', views.rawmaterialshow, name="rawmaterialshow"),
      path('recycle_show', views.recyclingshow, name="recyclingshow"),
      path('sales_show', views.salesshow, name="salesshow"),
      path('supplier_show', views.suppliershow, name="suppliershow"),
      path('work_show', views.workshow, name="workshow"),
    #   path('nav/',views.nav, name ='nav'),

    #   add
      path('admin_add/',views.admin_add, name ="admin_add"),
      path('category_add', views.category_add ,name="category_add"),
      path('customer_add/',views.customer_add, name ="customer_add"),
      path('delivery_add', views.delivery_add ,name="delivery_add"),
      path('purchase_add/',views.purchase_add, name ='purchase_add'),
      path('sup_add/',views.sup_add, name ="sup_add"), 
      path('work_add/',views.workform, name ='workform'),
      path('employee_add' ,views.employee_add,name="employee"),
      path('order_add' ,views.order_add,name="order"),
      path('billing_add' ,views.billing_add,name="billing"),
      path('feedback_add' ,views.feedback_add,name="feedback_add"),
      path('offer_add' ,views.offer_add,name="offer_add"),
      path('rawmaterial_add',views.rawmaterial_add,name="rawmaterial_add"),
      path('recycling_add',views.recycling_add,name="recycling_add"),
      path('production_add',views.production_add,name="production_add"),
      path('product_add',views.product_add,name="product_add"),
      path('sales_add',views.sales_add,name="sales"),
      path("stock_add", views.stock_add, name="stock_add")
      

      

      # delete
      path('delete_admin/<int:admin_id>', views.delete_admin ,name="delete_admin"),
      path('delete_billing/<int:bill_id>', views.delete_billing ,name="delete_billing"),
      path('delete_delivery/<int:d_id>', views.delete_delivery ,name="delete_delivery"),
]
