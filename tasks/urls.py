from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    #'loquesea/'
    path('', views.task_list, name='task-list'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit-task'),
    path('pending/', views.task_list_pending, name='task-list-pending'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
]
