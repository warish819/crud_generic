from django.urls import path
from taskapp import views
from taskapp.class_based_view import CreateTask, DeleteTask, ShowTask, UpdateTask


urlpatterns = [
    # path('',views.index),
    # path('show_task',views.show_task,name='show_task'),
    # path('update_task/<int:id>/',views.update_task,name='update_task'),
    # #path('update_status/<int:id>/',views.update_status,name='update_status'),
    # path('delete_task/<int:id>/',views.delete_task,name='delete_task'),
    path('',CreateTask.as_view()),
    path('show-task',ShowTask.as_view(),name='show-task'),
    path('update-task/<pk>/',UpdateTask.as_view(),name='update-task'),
    path('delete-task/<pk>/',DeleteTask.as_view(),name='delete-task')

    

]
