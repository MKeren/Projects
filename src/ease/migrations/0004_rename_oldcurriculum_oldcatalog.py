# Generated by Django 5.0.4 on 2024-05-14 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ease', '0003_oldcurriculum_newcatalog_total_credits_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OldCurriculum',
            new_name='OldCatalog',
        ),
    ]