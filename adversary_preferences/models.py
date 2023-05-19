from django.db import models

from adversary_groups.models import AdversaryGroup
from sub_techniques.models import SubTechnique
from tactics.models import Tactic
from techniques.models import Technique

# Create your models here.
class AdversaryGroupPreference(models.Model):
    adversary_group = models.ForeignKey(AdversaryGroup, on_delete=models.CASCADE)
    tactics = models.ForeignKey(Tactic, on_delete=models.CASCADE)
    techniques = models.ManyToManyField(Technique, limit_choices_to={'tactics__in': [tactics]})
    subtechniques = models.ManyToManyField(SubTechnique, blank=True, limit_choices_to={'technique__in': techniques})

    def __str__(self):
        return f"{self.adversary_group.group_name} - {self.tactic.tactic_name}"

