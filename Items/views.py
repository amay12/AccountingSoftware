from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Item, Tax
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from .forms import ItemForm, TaxForm


def tax_form_view(request):
    if request.method == 'POST':
        # return redirect('Details/ds.html')
        form = TaxForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            tax = Tax(
                username=username1,
                Tax_Name=cd['Tax_Name'],
                Tax_Rate=cd['Tax_Rate'],


            )
            tax.save()
            return redirect('Items:tax-add')
    else:
        form = TaxForm()
        return render(request, 'Items/tax_form.html', {'form': form})


def item_form_view(request):
    if request.method == 'POST':
        # return redirect('Details/ds.html')
        form = ItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            item = Item(
                username=username1,
                Item_Name=cd['Item_Name'],
                Item_Code=cd['Item_Code'],
                Unit_Price=cd['Unit_Price'],
                Description=cd['Description'],
                Purchases_Account=cd['Purchases_Account'],
                Tax_Rate=cd['Tax_Rate'],
                Quantity=cd['Quantity'],
                Selling_Price=cd['Selling_Price'],
                Status=cd['Status'],

            )
            item.save()
            return redirect('Items:item-index')
    else:
        form = ItemForm()
        return render(request, 'Items/item_form.html', {'form': form})


class ItemCreate(CreateView):
    model = Item
    fields = ['Item_Name', 'Item_Code',
              'Unit_Price', 'Description',
              'Purchases_Account', 'Tax_Rate',
              'Quantity', 'Selling_Price',
              'Status',
              ]


class ItemUpdate(UpdateView):
    model = Item
    fields = ['Item_Name', 'Item_Code',
              'Unit_Price', 'Description',
              'Purchases_Account', 'Tax_Rate',
              'Quantity', 'Selling_Price',
              'Status',
              ]


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('Items:item-index')


class ItemIndex(generic.ListView):
    template_name = 'Items/itemindex.html'

    def get_queryset(self):
        return Item.objects.filter(username=self.request.session['username'])


class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'Items/itemdetail.html'

