# Generated by Django 4.2.1 on 2023-05-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adversary_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adversarygroup',
            name='group_id',
            field=models.CharField(max_length=20, unique=True, verbose_name='Group ID'),
        ),
        migrations.AlterField(
            model_name='adversarygroup',
            name='group_name',
            field=models.CharField(max_length=150, verbose_name='Group Name'),
        ),
    ]
