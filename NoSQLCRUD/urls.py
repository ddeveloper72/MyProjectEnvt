from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_all_tasks, name='get_tasks')
    # path('', views.add_task, name='add_task'),
    
    ]