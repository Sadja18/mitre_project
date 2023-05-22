# Generated by Django 4.2.1 on 2023-05-22 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techniques', '0003_auto_20230522_0659'),
        ('adversary_preferences', '0004_alter_adversarygrouppreference_technique'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adversarygrouppreference',
            old_name='tactic',
            new_name='tactics',
        ),
        migrations.AlterField(
            model_name='adversarygrouppreference',
            name='technique',
            field=models.ForeignKey(limit_choices_to={'tactic': models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tactics.tactic')}, on_delete=django.db.models.deletion.CASCADE, to='techniques.technique'),
        ),
    ]
