
from django.urls import path
from .views import *

urlpatterns = [
   path('',show_emp,name='show_emp'),
   path('show_cus/',show_cus,name='show_cus'),
   path('add_employee/',add_employee,name='add_employee'),
   path('add_customer/',add_customer,name='add_customer'),
   path('delete_emp/<str:id>/',delete_emp,name='delete_emp'),
   path('delete_cust/<str:id>',delete_cust,name='delete_emp')
]
