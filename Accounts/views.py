from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BankAccount, Sales, Purchases
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import BankAccountForm, SalesForm, PurchasesForm


class SalesDelete(DeleteView):
    model = Sales
    success_url = reverse_lazy('Accounts:sales-index')


class PurchasesDelete(DeleteView):
    model = Purchases
    success_url = reverse_lazy('Accounts:purchases-index')


class SalesIndex(generic.ListView):
    template_name = 'Accounts/salesindex.html'

    def get_queryset(self):
        return Sales.objects.filter(username=self.request.session['username'])


class PurchasesIndex(generic.ListView):
    template_name = 'Accounts/purchasesindex.html'

    def get_queryset(self):
        return Purchases.objects.filter(username=self.request.session['username'])


def sales_form_view(request):
    if request.method == 'POST':
        form = SalesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            sales = Sales(
                username=username1,
                To=cd['To'],
                Date=cd['Date'],
                Due_Date=cd['Due_Date'],
                References=cd['References'],
                Amount=cd['Amount'],
                )
            sales.save()
            return redirect('Accounts:sales-index')
    else:
        form = SalesForm()
        return render(request, 'Accounts/salesaccount_form.html', {'form': form})


def purchases_form_view(request):
    if request.method == 'POST':
        form = PurchasesForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            purchases = Purchases(
                username=username1,
                From=cd['From'],
                Date=cd['Date'],
                Due_Date=cd['Due_Date'],
                References=cd['References'],
                Amount=cd['Amount'],
            )
            purchases.save()
            return redirect('Accounts:purchases-index')
    else:
        form = PurchasesForm()
        return render(request, 'Accounts/purchasesaccount_form.html', {'form': form})


def bankaccount_form_view(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username1 = request.session['username']
            bankaccount = BankAccount(
                username=username1,
                Bank_Name=cd['Bank_Name'],
                Account_No=cd['Account_No'],
                Description=cd['Description'],
                )
            bankaccount.save()
            return redirect('Accounts:bankaccount-index')
    else:
        form = BankAccountForm()
        return render(request, 'Accounts/bankaccount_form.html', {'form': form})


class BankAccountIndex(generic.ListView):
    template_name = 'Accounts/bankaccount_index.html'

    def get_queryset(self):
        return BankAccount.objects.filter(username=self.request.session['username'])


class BankAccountDelete(DeleteView):
    model = BankAccount
    success_url = reverse_lazy('Accounts:bankaccount-index')


