from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.loginPage,name='login'),
    path('register/', views.registerPage, name='register'),
    path('product/', views.product, name='product'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('createorder/<str:pk>/', views.createOrder, name='createorder'),
    path('updateorder/<str:pk>/', views.updateOrder, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteOrder, name='deleteorder'),
]
