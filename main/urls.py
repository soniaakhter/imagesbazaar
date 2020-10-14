from django.urls import path
from .views import *

urlpatterns = [
    
    path('aboutus/',show_about_page,name='about'),
    path('',show_home_page,name='home'),
    path('category/<int:id>/',show_category_page,name='category'),
    path('search/',search,name='search')
]
