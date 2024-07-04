from django.urls import path
from . import views
#/posts
app_name='todos'
# designated name for posts module


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.todos, name='todo_list'), # todos:todo_list
    path('submit-todo/', views.submit_todo, name='submit_todo'), # todos:submit_todo

    path('completed-todo/<int:pk>/', views.completed_todo, name='completed_todo'), # todos:submit_todo
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'), # todos:submit_todo
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'), # todos:submit_todo
]