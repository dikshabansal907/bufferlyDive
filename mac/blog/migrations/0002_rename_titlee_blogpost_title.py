# Generated by Django 3.2.8 on 2021-12-22 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='titlee',
            new_name='title',
        ),
    ]
