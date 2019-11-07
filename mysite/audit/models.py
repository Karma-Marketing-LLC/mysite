import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Lead(models.Model):
    """ This is the potential deal, it will gather as much information as
    automatically possible, it will then use that data to skip as
    many steps of the audit as possible with the present info.

     technical description here: """
    lead_title = models.CharField(verbose_name='Lead Name', max_length=35)

    def __str__(self):
        return self.lead_title


class Person(models.Model):
    """ This is the person you know.

    Do not send through both *args and **kwargs, send one or the other.
    person = Person(**kwargs)
    For the record, this is PROPER format for a docstring"""
    contact_name = models.CharField(verbose_name='Contact Name', max_length=50)
    met_d_time = models.DateTimeField('Meeting Date & Time')
    lead = models.ForeignKey(Lead, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.contact_name

    def was_met_today(self):
        return self.met_d_time >= timezone.now() - datetime.timedelta(days=1)


class Organization(models.Model):
    """ Each organization will be fed the necessary/possible parameters,
    then it will do as much of the audit and inspection as possible.

    technical description here: """
    lead = models.ForeignKey(Lead, null=True, blank=True, on_delete=models.SET_NULL)
    organization_name = models.CharField(verbose_name='Organization Name', max_length=50)
    month_rec_rev = models.PositiveIntegerField('Monthly Recurring Revenue')

    def __str__(self):
        return self.organization_name
