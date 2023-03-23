from django.urls import path

from . import views

urlpatterns = [
    path('get-tasks', views.get_tasks, name='get_tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('insert_task', views.insert_task, name='insert_task'),
    path('edit_task/<task_id>',
         views.edit_task, name='edit_task'),
    path('update_task/<task_id>',
         views.update_task, name='update_task'),
    path('delete_task/<task_id>',
         views.delete_task, name='delete_task'),
    path('get_categories', views.get_categories, name='get_categories'),
    path('edit_category/<category_id>',
         views.edit_category, name='edit_category'),
    path('update_category/<category_id>',
         views.update_category, name='update_category'),
    path('insert_category',
         views.insert_category, name='insert_category'),
    path('new_category',
         views.new_category, name='new_category'),
    path('delete_category/<category_id>',
         views.delete_category, name='delete_category')

]
