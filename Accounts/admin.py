from django.contrib import admin
from .models import BankAccount, Sales, Purchases

admin.site.register(BankAccount)
admin.site.register(Sales)
admin.site.register(Purchases)
