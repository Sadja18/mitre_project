from django.contrib import admin

from django.contrib.admin import widgets

from .models import AdversaryTechniques

class AdversaryTechniquesAdmin(admin.ModelAdmin):
    list_display = ['row_id', 'adversary_group', 'tactic', 'technique', 'sub_technique']
    list_filter = ['adversary_group', 'tactic', 'technique']

    autocomplete_fields = ['technique', 'sub_technique']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name in ['technique', 'sub_technique']:
            kwargs['widget'] = widgets.ForeignKeyRawIdWidget(db_field.remote_field, self.admin_site)
            kwargs['queryset'] = db_field.remote_field.model.objects.all()
            return db_field.formfield(**kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Media:
        js = [
            'admin/js/jquery.init.js',
            'autocomplete_light/jquery.init.js',
            'autocomplete_light/autocomplete.init.js',
        ]
        css = {
            'all': ['autocomplete_light/style.css'],
        }

admin.site.register(AdversaryTechniques, AdversaryTechniquesAdmin)