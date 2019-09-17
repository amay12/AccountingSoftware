from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import AllDetails
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import DetailForm
from django.contrib.auth.decorators import login_required



class DetailsUpdate(UpdateView):
    model = AllDetails
    fields = ['Gender', 'Gender',
              'Contact_no', 'Company_name',
              'DOB', 'Address',
              ]


@login_required()
def detail_show(request):
    username = request.session['username']
    objects = AllDetails.objects.filter(username=username).values()
    res = 'Printing all entries in the DB : <br>'

    #for elt in objects:
     #   res += elt.gender + "<br>"
    return render(request, 'Contacts/form_template.html', { 'objects' : objects})


class DetailUsername(generic.ListView):
    template_name = 'Details/DetailUsername.html'

    def get_queryset(self):
        return AllDetails.objects.filter(username=self.request.session['username'])

def saved(request):
    return redirect('Details:details-shownew')


@login_required()
def detail_form_view(request):
    if request.method == 'POST':
        # return redirect('Details/ds.html')
        form = DetailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            alldetails = AllDetails(
                username=username1,
                Gender=cd['Gender'],
                Contact_no=cd['Contact_no'],
                Company_name=cd['Company_name'],
                DOB=cd['DOB'],
                Address=cd['Address'],

            )
            alldetails.save()
            return redirect('Details:details-shownew')
    else:
        form = DetailForm()
        return render(request, 'Details/alldetails_form.html', {'form': form})

