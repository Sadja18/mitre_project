from django.contrib import admin
from .models import AdversaryGroup

# Register your models here.
class AdversaryGroupAdmin(admin.ModelAdmin):
    # list_filter = ['']
    list_display = ['group_id', 'group_name']
    search_fields = ['group_id', 'group_name']

admin.site.register(AdversaryGroup, AdversaryGroupAdmin)