from .views import CustomerList,CustomerDetail
from django.urls import path

urlpatterns = [
     path('customer/', CustomerList),
      path('customer/<int:pk>/', CustomerDetail),
]

