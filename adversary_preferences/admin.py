from django.contrib import admin

from django.contrib.admin.widgets import FilteredSelectMultiple

# Register your models here.
from .models import AdversaryGroupPreference

class AdversaryGroupPreferenceAdmin(admin.ModelAdmin):
    list_display = [
        'adversary_group',
        'tactics',
        'technique',
        'get_subtechniques'
        ]
    search_fields = [
        'adversary_group__group_name',
        'tactics__tactic_name',
        'technique__technique_name'
    ]

    @admin.display(description='Sub-Techniques')
    def get_subtechniques(self, obj):
        return ", ".join([st.subtechnique_name for st in obj.subtechniques.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'subtechniques':
            kwargs['widget'] = FilteredSelectMultiple('SubTechniques', is_stacked=False)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(AdversaryGroupPreference, AdversaryGroupPreferenceAdmin)