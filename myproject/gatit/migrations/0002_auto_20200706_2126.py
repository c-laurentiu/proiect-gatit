# Generated by Django 3.0.7 on 2020-07-06 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gatit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='ingredient',
            new_name='ingredient_name',
        ),
    ]
