# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from whiteeagle.utils import NamedObject

# Create your models here.
class Announcement(NamedObject):
    description = models.TextField()

    post_date = models.DateTimeField()
    expire_date = models.DateTimeField()