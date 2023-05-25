# Generated by Django 4.2.1 on 2023-05-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adversary_techniques', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adversarytechniques',
            options={'verbose_name': 'Adversary Technique', 'verbose_name_plural': 'Adversary Techniques'},
        ),
        migrations.AlterField(
            model_name='adversarytechniques',
            name='row_id',
            field=models.PositiveBigIntegerField(editable=False, unique=True),
        ),
    ]
