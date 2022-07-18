from django.urls import path 
from accounts import views



urlpatterns = [

    path('signup/', views.user_registration),
    path('login/', views.user_login),
    
]
