from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.task_list),
    path('delete/<int:id>/', views.delete_task),
    path('complete/<int:id>/', views.complete_task),
    path('api/tasks/', views.api_tasks),
]