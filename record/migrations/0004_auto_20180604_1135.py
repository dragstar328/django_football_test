# Generated by Django 2.0.5 on 2018-06-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0003_auto_20180604_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='remark',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='rival_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
