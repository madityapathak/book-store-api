# Generated by Django 5.0.6 on 2024-05-20 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='nane',
            new_name='name',
        ),
    ]
