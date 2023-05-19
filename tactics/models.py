from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Tactic(models.Model):
    tactic_id = models.CharField(verbose_name="Tactic ID", unique=True, null=False, blank=False, max_length=10)
    tactic_name = models.TextField(verbose_name="Tactic Name", null=False, blank=False, unique=False)

    def __str__(self):
        return str(self.tactic_id) + " :: " + str(self.tactic_name)
    
    class Meta:
        ordering = ['tactic_name',]