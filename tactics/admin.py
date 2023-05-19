from django.contrib import admin
from .models import Tactic

# Register your models here.
class TacticAdmin(admin.ModelAdmin):
    list_display = ('tactic_id', 'tactic_name')
    search_fields = ('tactic_id', 'tactic_name')

admin.site.register(Tactic, TacticAdmin)