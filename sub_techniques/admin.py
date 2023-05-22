from django.contrib import admin
# Register your models here.
from .models import SubTechnique

# admin.site.register(SubTechnique)
class SubTechniqueAdmin(admin.ModelAdmin):
    list_display = ('subtechnique_id','subtechnique_name', 'get_technique')
    search_fields = ['subtechnique_id', 'subtechnique_name', 'technique__technique_name', 'technique__technique_id']
    raw_id_fields = ['technique']    

    @admin.display(description='Technqiue Name')
    def get_technique(self, obj):
        return obj.technique.technique_name if obj.technique else None
    
admin.site.register(SubTechnique, SubTechniqueAdmin)