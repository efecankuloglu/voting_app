# Generated by Django 3.2.6 on 2021-08-29 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_auto_20210829_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='duration',
        ),
        migrations.AddField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
