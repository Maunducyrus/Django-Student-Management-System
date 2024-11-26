from django.urls import path

# from StudentSystem.urls import urlpatterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_students, name='view_student'),
]