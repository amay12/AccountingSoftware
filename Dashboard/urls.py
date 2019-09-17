from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'Dashboard'
urlpatterns = [

    # /contacts/index/
    url(r'^index/$', login_required(views.dashboard_view), name='dashboard-index'),


]