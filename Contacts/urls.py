from django.conf.urls import url
from . import views
from .models import AllContacts
from django.contrib.auth.decorators import login_required

app_name = 'Contacts'
urlpatterns = [

    # /contacts/index/
    url(r'index/$', login_required(views.ContactIndex.as_view()), name='contact-index'),

    # /contacts/consumer/
    url(r'consumer/$', login_required(views.ContactConsumer.as_view()), name='contact-consumer'),

    # /contacts/supplier/
    url(r'supplier/$', login_required(views.ContactSupplier.as_view()), name='contact-supplier'),

    # /contacts/add/
    url(r'add/$', login_required(views.contact_form_view), name='contact-add'),

    # /contacts/edit/2
    url(r'edit/(?P<pk>[0-9]+)/$', login_required(views.ContactUpdate.as_view()), name='contact-update'),

    # /contacts/edit/2/delete/
    url(r'edit/(?P<pk>[0-9]+)/delete/$', login_required(views.ContactDelete.as_view()), name='contact-delete'),

    # /contacts/2
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.ContactDetail.as_view()), name='contact-detail'),

]