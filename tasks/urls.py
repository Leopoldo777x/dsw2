from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    #'loquesea/'
    path('', views.task_list, name='task-list'),
    path('add/', views.add_task, name='add-task'),
    path('completed/', views.task_list_completed, name='task-list-completed'),
    path('pending/', views.task_list_pending, name='task-list-pending'),
    path('<slug:task_slug>/edit/', views.edit_task, name='edit-task'),
    path('<slug:task_slug>/delete/', views.delete_task, name='delete-task'),
    path('<slug:task_slug>/toggle/', views.toggle_task, name='toggle-task'),
    path('<slug:task_slug>/', views.task_detail, name='task-detail'),
]
