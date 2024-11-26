from django.urls import path

# from StudentSystem.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_students, name='view_student'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]