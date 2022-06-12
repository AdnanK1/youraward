from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.loginPage,name='login'),
    path('register',views.register,name='register'),

    path('home',views.home,name='home'),
    path('submission',views.submission,name='submission'),
    path('user',views.user,name='user'),
    path('profile',views.profile,name='profile'),
]