from django.contrib import admin
from django.forms import ModelForm, Select

from .models import AdversaryTechniques

class AdversaryTechniquesForm(ModelForm):
    class Meta:
        model = AdversaryTechniques
        fields = '__all__'
        widgets = {
            'technique': Select(attrs={'class': 'technique-select'}),
            'sub_technique': Select(attrs={'class': 'sub-technique-select'}),
        }

class AdversaryTechniquesAdmin(admin.ModelAdmin):
    list_display = ['adversary_group', 'tactic', 'technique', 'sub_technique']
    list_filter = ['adversary_group', 'tactic', 'technique']
    form = AdversaryTechniquesForm

    class Media:
        js = ('admin/custom.js',)

admin.site.register(AdversaryTechniques, AdversaryTechniquesAdmin)