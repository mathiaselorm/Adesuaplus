from . import views
from django.urls import path

urlpatterns = [
    path('', views.list_teachers, name='teachers'),
    path('create/', views.create_teacher, name='create-teacher'),
    path('retrieve/<str:pk>/', views.retrieve_teacher, name='retrieve-teacher'),
    path('update/<str:pk>/', views.update_teacher, name='update-teacher'),
    path('delete/<str:pk>/', views.delete_teacher, name='delete-teacher'),
]