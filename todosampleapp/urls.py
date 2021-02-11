from django.urls import path
from . import views

urlpatterns=[
    path('', views.task_view, name='task_view'),
    path('delete/<int:delete_id>/', views.delete, name='delete'),
    path('update/<int:update_id>/', views.update, name='update')

]