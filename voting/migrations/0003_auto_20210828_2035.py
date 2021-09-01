# Generated by Django 3.2.6 on 2021-08-28 17:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0002_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='created',
        ),
        migrations.AddField(
            model_name='question',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='question',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
