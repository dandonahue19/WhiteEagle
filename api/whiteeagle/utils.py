from django.db import models

class NamedObject(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name