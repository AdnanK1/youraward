from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.loginPage,name='login'),
    path('register',views.register,name='register'),

    path('home',views.home,name='home'),
    path('submission',views.submission,name='submission'),
    path('user',views.user,name='user'),
    path('profile/<str:pk>',views.profile,name='profile'),
    path('like/<str:pk>',views.likeProject,name='like_project'),

    path('api/project',views.ProjectList.as_view()),
    path('api/profile',views.ProfileList.as_view()),
]