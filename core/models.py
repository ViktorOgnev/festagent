from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Fest(models.Model):

    name = models.CharField(max_length=255, verbose_name=_("Fest"))
    country = models.CharField(max_length=255, verbose_name=_("Country"))
    biginning_date = models.DateTimeField(default=datetime.now(),   
                                          verbose_name=_("Date of the beginning"))
    class Meta:
        verbose_name = _("Festival")
        verbose_name_plural = _("Festivals")
    
    def __unicode__(self):
        return self.name
        
    
