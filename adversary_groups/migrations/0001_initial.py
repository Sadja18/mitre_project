# Generated by Django 4.2.1 on 2023-05-25 05:11

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdversaryGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.CharField(max_length=20, unique=True, verbose_name='ID')),
                ('group_name', models.CharField(max_length=150, verbose_name='Name')),
                ('associated_groups', models.TextField(blank=True, null=True, verbose_name='Associated Groups')),
                ('group_description', django_quill.fields.QuillField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Adversary Group',
                'verbose_name_plural': 'Adversary Groups',
                'ordering': ['group_id'],
            },
        ),
    ]
