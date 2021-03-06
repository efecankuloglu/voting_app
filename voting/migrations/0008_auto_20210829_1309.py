# Generated by Django 3.2.6 on 2021-08-29 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_alter_question_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='duration',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
