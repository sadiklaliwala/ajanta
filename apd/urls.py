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
    # path('',include('adminsite.urls'))
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
path()
]
