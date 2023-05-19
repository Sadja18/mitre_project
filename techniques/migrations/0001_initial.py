# Generated by Django 4.2.1 on 2023-05-19 06:14

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tactics', '0003_alter_tactic_tactic_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technique_id', models.CharField(max_length=50, unique=True, verbose_name='ID')),
                ('technique_name', models.CharField(max_length=100, verbose_name=True)),
                ('technique_description', django_quill.fields.QuillField(blank=True, null=True)),
                ('tactics', models.ManyToManyField(to='tactics.tactic')),
            ],
            options={
                'ordering': ['technique_name'],
            },
        ),
    ]