from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('form', views.form, name='form'),
    path('red', views.red, name='red'),
    path('order', views.order, name='order'),

]
