from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from Contacts.models import AllContacts


class BankAccount(models.Model):
    username = models.CharField(max_length=50)
    Bank_Name = models.CharField(max_length=50)
    Account_No = models.CharField(max_length=50)
    Description =  models.CharField(max_length=250)

    def __str__(self):
        return self.username + "-" + self.Bank_Name

   # def get_absolute_url(self):
   #    return reverse('', kwargs={'pk': self.pk})

    class Admin:
        pass


class Sales(models.Model):
    username = models.CharField(max_length=50)
    To = models.ForeignKey(AllContacts, on_delete=models.CASCADE)
    Date = models.DateField()
    Due_Date = models.DateField()
    References = models.CharField(max_length=250)
    Amount = models.CharField(max_length=50)

    def __str__(self):
        return self.username + "-" + self.To

   # def get_absolute_url(self):
   #    return reverse('', kwargs={'pk': self.pk})

    class Admin:
        pass


class Purchases(models.Model):
    username = models.CharField(max_length=50)
    From = models.ForeignKey(AllContacts, on_delete=models.CASCADE)
    Date = models.DateField()
    Due_Date = models.DateField()
    References = models.CharField(max_length=50)
    Amount = models.CharField(max_length=250)

    def __str__(self):
        return self.username + "-" + self.From

   # def get_absolute_url(self):
   #    return reverse('', kwargs={'pk': self.pk})

    class Admin:
        pass
