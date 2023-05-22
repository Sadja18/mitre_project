from django.db import models

from techniques.models import Technique

# Create your models here.
class SubTechnique(models.Model):
    subtechnique_id = models.CharField(max_length=50, unique=False, verbose_name="ID")
    subtechnique_name = models.CharField(max_length=100, verbose_name="Name")
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtechnique_name
    
    class Meta:
        verbose_name = "Sub Technique"
        verbose_name_plural = "Sub Techniques"