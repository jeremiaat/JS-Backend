from django.contrib import admin
from .models import Drawings,ContactInfo,Order,PriceList,ExhibitedWorks
# Register your models here.

admin.site.register(Drawings)
admin.site.register(Order)
admin.site.register(PriceList)
admin.site.register(ExhibitedWorks)
admin.site.register(ContactInfo)

class DrawingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'created_at')
    list_filter = ('year',)
    ordering = ('year', 'created_at')

    def year_display(self, obj):
        return obj.date.year
    
    year_display.short_description = 'Year'