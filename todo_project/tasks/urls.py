from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.task_list),
    path('register/', views.register),
    path('login/', LoginView.as_view(template_name='tasks/login.html')),
    path('logout/', LogoutView.as_view()),
    path('delete/<int:id>/', views.delete_task),
    path('complete/<int:id>/', views.complete_task),
    path('api/tasks/', views.api_tasks),
]