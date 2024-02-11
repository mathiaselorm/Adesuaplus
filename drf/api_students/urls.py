from . import views
from django.urls import path
urlpatterns = [
    path('students-list/', views.list_students, name='students-list'),
    path('create-student/', views.create_student, name='create-student'),
    path('retrieve/student/<str:pk>/', views.retrieve_student, name='retrieve-student'),
    path('update/student/<str:pk>/', views.update_student, name='update-student'),
    path('delete/student/<str:pk>/', views.delete_student, name='delete-student'),
]