# Generated by Django 4.2.5 on 2023-09-11 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='age',
        ),
        migrations.RemoveField(
            model_name='person',
            name='color',
        ),
        migrations.RemoveField(
            model_name='person',
            name='height',
        ),
        migrations.RemoveField(
            model_name='person',
            name='occupation',
        ),
    ]