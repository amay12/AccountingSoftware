from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
COUNTRY = (
    ('India', 'India'),
    ('USA', 'USA'),
    ('UK', 'UK'),
    ('Australia', 'Australia'),
    ('Sweden', 'Sweden'),
)

STATE = (
    ('State1', 'State1'),
    ('State2', 'State2'),
)
TYPE = (
    ('Consumer', 'Consumer'),
    ('Supplier', 'Supplier'),
)


class AllContacts(models.Model):
    username = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Primary_First_name = models.CharField(max_length=50)
    Primary_Last_name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact_No = models.CharField(max_length=20)
    Address= models.CharField(max_length=250)
    Contact_Type = models.CharField(max_length=20, choices=TYPE)
    Contact_Group = models.CharField(max_length=50)

    def __str__(self):
        return self.Company_Name + "-" + self.Primary_First_name

    def get_absolute_url(self):
        return reverse('Contacts:contact-detail', kwargs={'pk': self.pk})

    class Admin:
        pass
