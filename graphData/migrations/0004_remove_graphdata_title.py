# Generated by Django 3.0.2 on 2020-01-17 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphData', '0003_auto_20200117_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphdata',
            name='title',
        ),
    ]
