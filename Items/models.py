from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from Contacts.models import AllContacts

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


class Tax(models.Model):
    username = models.CharField(max_length=50)
    Tax_Name = models.CharField(max_length=50)
    Tax_Rate = models.CharField(max_length=4) # Also Check for Compound Tax

    def __str__(self):
        return self.Tax_Name + "-" + self.Tax_Rate+"%"


class Item(models.Model):
    username = models.CharField(max_length=50)
    Item_Name = models.CharField(max_length=50)
    Item_Code = models.CharField(max_length=50)
    Unit_Price = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Purchases_Account = models.CharField(max_length=50, choices=PA)
    # Tax_Rate = models.CharField(max_length=10)
    Tax_Rate = models.ForeignKey(Tax, on_delete=models.CASCADE)
    Quantity = models.CharField(max_length=10)
    Selling_Price = models.CharField(max_length=10)
    Status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.Item_Name + "-" + self.Item_Code

    def get_absolute_url(self):
        return reverse('Items:item-detail', kwargs={'pk' : self.pk})

    class Admin:
        pass