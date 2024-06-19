

from django.urls import path
from . import views
#/posts
app_name='posts'
# designated name for posts module


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.posts_list, name='list'), # posts:list
    path('new-post/',views.post_new,name='new-post'),
    path('<slug:slug>', views.post_page, name='page'), #posts:page
]