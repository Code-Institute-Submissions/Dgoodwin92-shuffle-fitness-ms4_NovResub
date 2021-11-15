from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_memberships, name='memberships'),
    path('<int:membership_id>/', views.membership_detail, name='membership_detail'),
    path('add/', views.add_membership, name='add_membership'),
    path('edit/<int:membership_id>/', views.edit_membership, name='edit_membership'),
]
