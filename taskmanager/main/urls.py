from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('admin', views.admin, name='admin'),
    path('address/<int:item_id>', views.address, name='address'),
    path('reviews/<int:item_id>', views.reviews, name='reviews'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('grade', views.grade, name='grade'),
]
