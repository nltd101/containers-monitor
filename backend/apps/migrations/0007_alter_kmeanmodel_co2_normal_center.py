# Generated by Django 3.2.9 on 2021-11-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_merge_0005_auto_20211103_0811_0005_auto_20211105_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kmeanmodel',
            name='co2_normal_center',
            field=models.FloatField(null=True),
        ),
    ]
