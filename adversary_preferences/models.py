from django.db import models

from adversary_groups.models import AdversaryGroup
from sub_techniques.models import SubTechnique
from tactics.models import Tactic
from techniques.models import Technique

# Create your models here.
class AdversaryGroupPreference(models.Model):
    adversary_group = models.ForeignKey(AdversaryGroup, on_delete=models.CASCADE)
    tactics = models.ForeignKey(Tactic, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.CASCADE)
    subtechniques = models.ManyToManyField(SubTechnique, blank=True)

    def __str__(self):
        return f"{self.adversary_group.group_name}"

