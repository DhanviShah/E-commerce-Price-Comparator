from django.urls import path
from .views import  *

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('contactUs/',contactUs,name='contactUs'),
    path('faq/',faq,name='faq'),
    path('about/',about,name='about'),
    path('logout/',logout,name='logout'),
    path('update/',update,name='update'),
    path('signup/',signup,name='signup'),
    path('product/<str:product>',product,name='product'),
    path('<str:search>/',p_list,name= 'list'),
]

