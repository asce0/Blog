from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.post_creation, name='post_creation'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('register-form/', views.register_form, name='register_form'),
]
