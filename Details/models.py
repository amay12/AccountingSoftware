from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.sessions.models import Session


GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class AllDetails(models.Model):
    username = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50, choices=GENDER)
    Contact_no = models.CharField(max_length=12)
    Company_name = models.CharField(max_length=50)
    DOB = models.DateField()
    Address = models.CharField(max_length=250)

    def __str__(self):
        return self.username + " Details"

    def get_absolute_url(self):
        return reverse('Details:details-saved')

    class Admin:
        pass

