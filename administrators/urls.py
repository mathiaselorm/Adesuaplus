from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_administrators, name='administrators'),
    path('create/', views.create_administrator, name='create-administrator'),
    path('retrieve/<str:pk>/', views.retrieve_administrator, name='retrieve-administrator'),
    path('update/<str:pk>/', views.update_administrator, name='update-administrator'),
    path('delete/<str:pk>/', views.delete_administrator, name='delete-administrator'),
]