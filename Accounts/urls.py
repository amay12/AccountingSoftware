from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'Accounts'

urlpatterns = [

    # /accounts/add/
    url(r'^add/$', login_required(views.bankaccount_form_view), name='bankaccount-add'),

    # /accounts/baindex/
    url(r'^baindex/$', login_required(views.BankAccountIndex.as_view()), name='bankaccount-index'),

    # /accounts/edit/2/delete/
    url(r'^edit/(?P<pk>[0-9]+)/delete/$', login_required(views.BankAccountDelete.as_view()), name='bankaccount-delete'),

    # /accounts/sales/index/
    url(r'sales/index/$', login_required(views.SalesIndex.as_view()), name='sales-index'),

    # /accounts/purchases/index/
    url(r'purchases/index/$', login_required(views.PurchasesIndex.as_view()), name='purchases-index'),

    # /accounts/sales/add/
    url(r'sales/add/$', login_required(views.sales_form_view), name='sales-add'),

    # /accounts/purchases/add/
    url(r'purchases/add/$', login_required(views.purchases_form_view), name='purchases-add'),

    # /accounts/sales/edit/2/delete/
    url(r'sales/edit/(?P<pk>[0-9]+)/delete/$', login_required(views.SalesDelete.as_view()), name='sales-delete'),

    # /accounts/purchases/edit/2/delete/
    url(r'purchases/edit/(?P<pk>[0-9]+)/delete/$', login_required(views.PurchasesDelete.as_view()), name='purchases-delete'),


]