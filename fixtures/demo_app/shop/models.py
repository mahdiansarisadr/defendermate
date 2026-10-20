from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(_("name"), max_length=200)
    attributes = JSONField(default=dict)
    discontinued = models.NullBooleanField()

    class Meta:
        index_together = [["name", "discontinued"]]
