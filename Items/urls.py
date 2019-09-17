from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'Items'
urlpatterns = [

    # /items/add/
    url(r'add/$', login_required(views.item_form_view), name='item-add'),

    # /items/addtax/
    url(r'addtax/$', login_required(views.tax_form_view), name='tax-add'),

    # /items/index/
    url(r'index/$', login_required(views.ItemIndex.as_view()), name='item-index'),

    # /items/edit/2
    url(r'edit/(?P<pk>[0-9]+)/$', login_required(views.ItemUpdate.as_view()), name='item-update'),

    # /items/edit/2/delete/
    url(r'edit/(?P<pk>[0-9]+)/delete/$', login_required(views.ItemDelete.as_view()), name='item-delete'),

    # /items/2
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.ItemDetail.as_view()), name='item-detail'),



]