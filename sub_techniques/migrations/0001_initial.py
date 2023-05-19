# Generated by Django 4.2.1 on 2023-05-19 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('techniques', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubTechnique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtechnique_id', models.CharField(max_length=50, unique=True, verbose_name='ID')),
                ('subtechnique_name', models.CharField(max_length=100, verbose_name='Name')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='techniques.technique')),
            ],
        ),
    ]