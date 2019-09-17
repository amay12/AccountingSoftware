from django.conf.urls import url
from . import views


app_name = 'register'
urlpatterns = [

    # /register/index/
    url(r'index/$', views.UserFormView.as_view(), name='register'),
    url(r'login/$', views.LoginFormView.as_view(), name='login'),
    url(r'home/$', views.logout_view, name='logout'),





]