from django.contrib import admin
from django.urls import path, include   # 👈 أضفنا include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),   # 👈 هذا السطر المهم
]