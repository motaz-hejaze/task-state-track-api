from . import views
from django.urls import path

urlpatterns = [
    path('task/create_new_task' , views.create_task),
    path('task/get_new_task/<id>' , views.get_task),
    path('task/edit_new_task' , views.edit_task),
    path('task/link_two_tasks' , views.link_tasks),
    path('task/show_linked_task/<id>' , views.show_linked_task),
    path('task/change_task_state' , views.change_task_state),
]