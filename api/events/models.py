# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest.util import _MAX_LENGTH
from django.db import models
from whiteeagle.utils import NamedObject

# Create your models here.
class EventType(NamedObject):
    color = models.CharField(max_length=12)

class Event(NamedObject):
    '''
    dt - dte for special events
    '''
    dt = models.DateTimeField(null=True, blank=True)
    dt_end = models.DateTimeField(null=True, blank=True)

    '''
    dow and time, ever for reoccuring events
    '''
    reoccuring = models.BooleanField(default=False)
    dow = models.IntegerField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=250)
    type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True)