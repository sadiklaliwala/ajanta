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

      # delete
      path('delete_admin/<int:admin_id>', views.delete_admin ,name="delete_admin"),
      path('delete_billing/<int:bill_id>', views.delete_billing ,name="delete_billing"),
      path('delete_delivery/<int:d_id>', views.delete_delivery ,name="delete_delivery"),

]
