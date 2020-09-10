from django.urls import include, path
from rest_framework import routers
from knox import views as knox_views

from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)
router.register(r'tasks', views.TaskViewSet, basename='tasks')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterViewSet.as_view(), name='register'),
    path('change-password/', views.ChangePasswordViewSet.as_view(), name='change_password'),
    path('login/', views.LoginViewSet.as_view(), name='login'),
    path('movie/', views.LiveMovieViewSet, name='movie'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logout/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += router.urls
