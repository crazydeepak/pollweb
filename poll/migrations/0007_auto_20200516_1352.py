# Generated by Django 3.0.4 on 2020-05-16 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20200516_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='secs_for_first_response',
            field=models.DecimalField(decimal_places=5, max_digits=8),
        ),
    ]
