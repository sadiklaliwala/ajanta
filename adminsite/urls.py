from django.contrib import admin
from django.urls import path
from adminsite import views

urlpatterns = [
      #all data show 
      path('show/',views.show, name ="show"),
      
      # navbar
      path('nav/',views.nav, name ='nav'),

      path('admindasheboard/', views.admindasheboard,name="admindasheboard"),
      
      # purchaseform
      path('purchase_add/',views.purchase_add, name ='purchase_add'),
      
      #work
      path('workform/',views.workform, name ='workform'),
      
      #customer
      path('customer_add/',views.customer_add, name ="customer_add"),
      
      # supplier 
      path('sup_add/',views.sup_add, name ="sup_add"),
      
      # admin 
      path('admin_add/',views.admin_add, name ="admin_add"),

      
      #delete
      path('delete_admin/<int:admin_id>', views.delete_admin ,name="delete_admin"),
      path('delete_billing/<int:bill_id>', views.delete_billing ,name="delete_billing"),
      path('delete_category/<int:category_id>', views.delete_category ,name="delete_category"),
      path('delete_customer/<int:customer_id>', views.delete_customer ,name="delete_customer"),
      path('delete_delivery/<int:d_id>', views.delete_delivery ,name="delete_delivery"),
      path('delete_employee/<int:emp_id>', views.delete_employee ,name="delete_employee"),
      path('delete_feedback/<int:f_id>', views.delete_feedback ,name="delete_feedback"),
      path('delete_offer/<int:offer_id>', views.delete_offer ,name="delete_offer"),
      path('delete_order/<int:order_id>', views.delete_order ,name="delete_order"),
      path('delete_production/<int:production_id>', views.delete_production ,name="delete_production"),
      path('delete_product/<int:product_id>', views.delete_product ,name="delete_product"),
      path('delete_purchase/<int:purchase_id>', views.delete_purchase ,name="delete_purchase"),
      path('delete_rawmaterial/<int:raw_id>', views.delete_rawmaterial ,name="delete_rawmaterial"),
      path('delete_recycle/<int:r_id>', views.delete_recycle ,name="delete_recycle"),
      path('delete_sale/<int:sales_id>', views.delete_sale ,name="delete_sale"),
      path('delete_stock/<int:stock_id>', views.delete_stock ,name="stock"),
      path('delete_supplier/<int:sup_id>', views.delete_supplier ,name="delete_supplier"),
      path('delete_work/<int:work_id>', views.delete_work ,name="delete_work"),

]
