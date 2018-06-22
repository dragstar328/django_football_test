# Generated by Django 2.0.5 on 2018-06-04 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20180604_1135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sebango', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('passes', models.IntegerField(default=0)),
                ('intercepts', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='rival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rival', to='record.Rival'),
        ),
        migrations.AddField(
            model_name='stats',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='record.Game'),
        ),
        migrations.AddField(
            model_name='stats',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='record.Player'),
        ),
    ]