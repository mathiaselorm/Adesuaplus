from . import views
from django.urls import path
urlpatterns = [
    path('list_students/', views.list_students, name='students'),
    path('create_student/', views.create_student, name='create_student'),
    path('retrieve_student/<str:pk>/', views.retrieve_student, name='retrieve_student'),
    path('update_student/<str:pk>/', views.update_student, name='students_update'),
    path('delete_student/<str:pk>/', views.delete_student, name='students_delete'),
]