from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AllContacts
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import ContactAddForm
from django.contrib.auth.decorators import login_required

@login_required()
def contact_form_view(request):
    if request.method == 'POST':
        # return redirect('Details/ds.html')
        form = ContactAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            allcontacts = AllContacts(
                username=username1,
                Company_Name=cd['Company_Name'],
                Primary_First_name=cd['Primary_First_name'],
                Primary_Last_name=cd['Primary_Last_name'],
                Email=cd['Email'],
                Contact_No=cd['Contact_No'],
                Address=cd['Address'],
                Contact_Type=cd['Contact_Type'],
                Contact_Group=cd['Contact_Group'],

            )
            allcontacts.save()
            return redirect('Contacts:contact-index')
    else:
        form = ContactAddForm()
        return render(request, 'Contacts/allcontacts_form.html', {'form': form})


@login_required()
def dashboard(request):
    t= get_template('Contacts/dashboard_template.html')
    return render(request, t)


@login_required()
class ContactCreate(CreateView):
    model = AllContacts
    fields = ['Company_Name', 'Primary_First_name',
              'Primary_Last_name', 'Email',
              'Contact_No', 'Country',
              'State', 'Address_Lane',
              'Contact_Type', 'Contact_Group',
              ]


class ContactUpdate(UpdateView):
    model = AllContacts
    fields = ['Company_Name', 'Primary_First_name',
              'Primary_Last_name', 'Email',
              'Contact_No', 'Address',
              'Contact_Type', 'Contact_Group',
              ]


class ContactDelete(DeleteView):
    model = AllContacts
    success_url = reverse_lazy('Contacts:contact-index')


class ContactIndex(generic.ListView):
    template_name = 'Contacts/contactindex.html'

    def get_queryset(self):
        return AllContacts.objects.filter(username=self.request.session['username'])


class ContactConsumer(generic.ListView):
    template_name = 'Contacts/contactconsumer.html'

    def get_queryset(self):
        return AllContacts.objects.filter(Contact_Type='Consumer', username=self.request.session['username'])


class ContactSupplier(generic.ListView):
        template_name = 'Contacts/contactsupplier.html'

        def get_queryset(self):
            return AllContacts.objects.filter(Contact_Type='Supplier', username=self.request.session['username'])


class ContactDetail(generic.DetailView):
    model = AllContacts
    template_name = 'Contacts/contactdetail.html'

