from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class AdversaryGroup(models.Model):
    group_id = models.CharField(verbose_name="ID", blank=False, null=False,unique=True, max_length=20)
    group_name = models.CharField(verbose_name="Name", blank=False, null=False,unique=False, max_length=150)
    associated_groups = models.TextField(verbose_name="Associated Groups", null=True, blank=True, unique=False)
    group_description = QuillField(blank=True, null=True)

    class Meta:
        verbose_name = "Adversary Group"
        verbose_name_plural = "Adversary Groups"
        ordering = ["group_id",]

    def __str__(self):
        return str(self.group_id) +  " " + str(self.group_name)