from django import forms
from .models import Item, Tax

STATUS = (
    ('Available', 'Available'),
    ('Out of Stock', 'Out of Stock'),
)
PA = (
    ('Discount', 'Discount'),
    ('General Income', 'General Income'),
    ('Late Fee Income', 'Late Fee Income'),
    ('Interest Income', 'Interest Income'),
    ('Other Charges', 'Other Charges'),
    ('Sales', 'Sales'),
    ('Shipping Charge', 'Shipping Charge'),


)


class TaxForm(forms.Form):
    Tax_Name = forms.CharField(max_length=50)
    Tax_Rate = forms.CharField(max_length=4, initial='5', label='Tax Rate (in Percents)')


class ItemForm(forms.Form):
    Item_Name = forms.CharField(max_length=50)
    Item_Code = forms.CharField(max_length=50)
    Unit_Price = forms.CharField(max_length=50)
    Description = forms.CharField(max_length=100)
    Purchases_Account = forms.ChoiceField(choices=PA)

    Tax_Rate = forms.ModelChoiceField(queryset=Tax.objects.all())
    Quantity = forms.CharField(max_length=10)
    Selling_Price = forms.CharField(max_length=10)
    Status = forms.ChoiceField(choices=STATUS)

    class meta:
        model= Item