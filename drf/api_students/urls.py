from . import views
from django.urls import path
urlpatterns = [
    path('', views.list_students, name='students'),
    path('create/', views.create_student, name='create-student'),
    path('retrieve/<str:pk>/', views.retrieve_student, name='retrieve-student'),
    path('update/<str:pk>/', views.update_student, name='update-student'),
    path('delete/<str:pk>/', views.delete_student, name='delete-student'),
]