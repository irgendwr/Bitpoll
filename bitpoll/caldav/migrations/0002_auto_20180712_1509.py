# Generated by Django 2.0.7 on 2018-07-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caldav', '0001_initial_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davcalendar',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterUniqueTogether(
            name='davcalendar',
            unique_together=set(),
        ),
    ]
