from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<membership_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<membership_id>/', views.remove_from_bag,
         name='remove_from_bag'),
]
