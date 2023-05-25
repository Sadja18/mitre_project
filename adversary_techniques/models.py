from django.db import models

from adversary_groups.models import AdversaryGroup
from tactics.models import Tactic
from techniques.models import Technique
from sub_techniques.models import SubTechnique

# Create your models here.
class AdversaryTechniques(models.Model):
    row_id = models.PositiveBigIntegerField(editable=False, unique=True)
    adversary_group = models.ForeignKey(AdversaryGroup, on_delete=models.CASCADE)
    tactic = models.ForeignKey(Tactic, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    sub_technique = models.ForeignKey(SubTechnique, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.adversary_group.group_name + "_" + self.tactic.tactic_name + "_" + self.technique.technique_name + "_" + str(self.sub_technique)
    
    def save(self, *args, **kwargs):
        if not self.pk:
            # Only set the row_id if the object is being created
            last_row_id = AdversaryTechniques.objects.order_by('-row_id').first()
            if last_row_id:
                self.row_id = last_row_id.row_id + 1
            else:
                self.row_id = 1

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Adversary Technique"
        verbose_name_plural = "Adversary Techniques"
