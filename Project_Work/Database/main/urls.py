from django.urls import path
from .views import home,login,logout,signup,product

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),
    path('product/<str:product>',product,name='product'),
]

