# Generated by Django 3.0.4 on 2020-05-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20200513_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollmodel',
            name='url_id',
            field=models.URLField(),
        ),
    ]