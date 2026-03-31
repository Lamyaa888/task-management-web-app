from django.urls import path
from .views import task_list, add_task, edit_task, delete_task, register
from django.contrib.auth import views as auth_views
from .views import task_list, add_task, edit_task, delete_task, register, toggle_complete
urlpatterns = [
    path('', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('toggle/<int:task_id>/', toggle_complete, name='toggle_complete'),
]