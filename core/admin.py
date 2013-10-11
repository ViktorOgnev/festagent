from django.contrib import admin
from .models import Fest

class FestAdmin(admin.ModelAdmin):

    
    list_per_page = 30
    ordering = ['name', 'biginning_date']
    search_fields = ['name', 'biginning_date', 'country']
        

admin.site.register(Fest, FestAdmin)