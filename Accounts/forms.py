from django import forms
from Contacts.models import AllContacts


class BankAccountForm(forms.Form):
    Bank_Name = forms.CharField(max_length=50)
    Account_No = forms.CharField(max_length=50)
    Description = forms.CharField(max_length=250)


class SalesForm(forms.Form):
    To = forms.ModelChoiceField(queryset=AllContacts.objects.all())
    Date = forms.DateField()
    Due_Date = forms.DateField()
    References = forms.CharField(max_length=250)
    Amount = forms.CharField(max_length=50)


class PurchasesForm(forms.Form):
    From = forms.ModelChoiceField(queryset=AllContacts.objects.all())
    Date = forms.DateField()
    Due_Date = forms.DateField()
    References = forms.CharField(max_length=250)
    Amount = forms.CharField(max_length=50)