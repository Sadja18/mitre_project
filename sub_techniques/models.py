from django.db import models

from django_quill.fields import QuillField

from techniques.models import Technique

# Create your models here.
class SubTechnique(models.Model):
    subtechnique_id = models.CharField(max_length=50, unique=True, verbose_name="ID")
    subtechnique_name = models.CharField(max_length=100, verbose_name="Name")
    subtechnique_description = QuillField(verbose_name="Description", null=True, blank=True)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtechnique_name
    
    def save(self, *args, **kwargs):
        if self.technique:
            technique_id = self.technique.technique_id
            subtechnique_id = self.subtechnique_id

            if technique_id in subtechnique_id:
                print(subtechnique_id)
                print(technique_id)
                super().save(*args, **kwargs)
                
            else:
                self.subtechnique_id = f"{self.technique.technique_id}.{self.subtechnique_id}"
                super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Sub Technique"
        verbose_name_plural = "Sub Techniques"