from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError


# Register your models here.
from .models import SubTechnique

# admin.site.register(SubTechnique)
class SubTechniqueAdmin(admin.ModelAdmin):
    list_display = ('subtechnique_id','subtechnique_name', 'get_technique')
    list_filter = ['technique']
    search_fields = ['subtechnique_id', 'subtechnique_name', 'technique__technique_name', 'technique__technique_id']
    # raw_id_fields = ['technique']    

    @admin.display(description='Technqiue Name')
    def get_technique(self, obj):
        return obj.technique.technique_name if obj.technique else None
    
    def save_model(self, request, obj, form, change):
        subtechnique_id = str(obj.technique).split()[0] + "." + str(obj.subtechnique_id)
        print(subtechnique_id)
        existing_subtechnique = SubTechnique.objects.filter(subtechnique_id=subtechnique_id).exists()
        print(existing_subtechnique)

        if existing_subtechnique:
            # Perform your validation check here
            # For example, raise a ValidationError or add an error to the form
            form.add_error('subtechnique_id', 'This sub-technique already exists.')
        else:
            super().save_model(request, obj, form, change)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'technique':
            kwargs['widget'] = admin.widgets.ForeignKeyRawIdWidget(db_field.remote_field, self.admin_site)

            obj = kwargs.get('obj')
            if obj:
                try:
                    kwargs['initial'] = obj.technique_id
                except ObjectDoesNotExist:
                    pass

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
    
admin.site.register(SubTechnique, SubTechniqueAdmin)