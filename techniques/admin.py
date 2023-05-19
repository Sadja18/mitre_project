from typing import Any, Optional
from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db.models.fields.related import ManyToManyField
from django.forms.models import ModelMultipleChoiceField
from django.http.request import HttpRequest
from django.urls import reverse

# Register your models here.
from .models import Technique

# admin.site.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ('technique_id', 'technique_name', 'get_tactics')
    search_fields = ['technique_name', 'technique_id']

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'tactics':
            kwargs['widget'] = FilteredSelectMultiple("Tactics", is_stacked=False)
        
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    @admin.display(description='Tactics')
    def get_tactics(self, obj):
        return ", ".join([tactic.tactic_name for tactic in obj.tactics.all()])


admin.site.register(Technique, TechniqueAdmin)