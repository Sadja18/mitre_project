from django.db import models

from django_quill.fields import QuillField

from tactics.models import Tactic

# Create your models here.
class Technique(models.Model):
    technique_id = models.CharField(max_length=50, unique=True, verbose_name="ID")
    technique_name = models.CharField(max_length=100, verbose_name=True)
    technique_description = QuillField(blank=True, null=True)
    tactics = models.ManyToManyField(Tactic)

    def __str__(self):
        return self.technique_name
    
    class Meta:
        ordering = ["technique_name",]