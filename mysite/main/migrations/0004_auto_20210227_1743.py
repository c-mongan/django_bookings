# Generated by Django 3.1.5 on 2021-02-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210227_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='details',
            field=models.TextField(blank=True, max_length=20, verbose_name='Details'),
        ),
    ]
