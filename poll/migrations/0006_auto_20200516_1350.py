# Generated by Django 3.0.4 on 2020-05-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_auto_20200516_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='secs_for_first_response',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]
