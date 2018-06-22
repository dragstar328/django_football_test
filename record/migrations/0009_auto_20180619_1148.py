# Generated by Django 2.0.5 on 2018-06-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_auto_20180619_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stats',
            name='remark',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='tuckle',
        ),
        migrations.AddField(
            model_name='stats',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='stats',
            name='tuckles',
            field=models.IntegerField(default=0),
        ),
    ]