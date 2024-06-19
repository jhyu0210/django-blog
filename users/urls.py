
from django.urls import path
from . import views
#/posts
app_name='users'
# designated name for posts module


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', views.register_view, name='register'), # users:register
    path('login/', views.login_view, name='login'), # users:login
    path('logout/', views.logout_view, name='logout'), # users:logout
    
]