from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'Details'
urlpatterns = [

    # /Details/add/
    # url(r'add/$', views.DetailsCreate.as_view(), name='details-add'),
    url(r'^newadd/$', login_required(views.detail_form_view), name='details-newadd'),
    url(r'^saved/$', login_required(views.saved), name='details-saved'),
    url(r'^show/$', login_required(views.detail_show), name='details-show'),
    url(r'^shownew/$', login_required(views.DetailUsername.as_view()), name='details-shownew'),
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(views.DetailsUpdate.as_view()), name='details-update'),


]