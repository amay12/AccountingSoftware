from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
from Contacts.models import AllContacts
from Items.models import Item,Tax
from Accounts.models import Sales,Purchases,BankAccount
from Details.models import AllDetails


def dashboard_view(request):
    username = request.session['username']
    consumers = AllContacts.objects.filter(Contact_Type='Consumer', username=username).count()
    suppliers = AllContacts.objects.filter(Contact_Type='Supplier', username=username).count()
    taxes = Tax.objects.filter(username=username)
    tax_count = Tax.objects.filter(username=username).count()
    items = Item.objects.filter(username=username)
    item_count = Item.objects.filter(username=username).count()
    sales = Sales.objects.filter(username=username)
    purchases = Purchases.objects.filter(username=username)
    sales_count = Sales.objects.filter(username=username).count()
    purchases_count = Purchases.objects.filter(username=username).count()
    data = {
        'consumers': consumers,
        'suppliers': suppliers,
        'Taxes': taxes,
        'Items': items,
        'tax_count': tax_count,
        'item_count': item_count,
        'sales': sales,
        'purchases': purchases,
        'sales_count': sales_count,
        'purchases_count': purchases_count,
    }
    template_name = 'Dashboard/index.html'
    return render(request, template_name, data)



