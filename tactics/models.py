from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class Tactic(models.Model):
    tactic_id = models.CharField(verbose_name="ID", unique=True, null=False, blank=False, max_length=10)
    tactic_name = models.TextField(verbose_name="Name", null=False, blank=False, unique=False)
    tactic_description = QuillField()

    def __str__(self):
        return str(self.tactic_id) + " :: " + str(self.tactic_name)
    
    class Meta:
        ordering = ['tactic_name',]