from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_all_tasks, name='get_tasks'),
    path('edit_task/<task_id>', views.edit_task, name='edit_task'),
    # path('insert_task/<task_id>', views.insert_task, name='insert_task')

]
