# Generated by Django 4.2.1 on 2023-05-13 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Weather', '0002_parsersetting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherkiev',
            old_name='temperature',
            new_name='temperature_day',
        ),
        migrations.AddField(
            model_name='weatherkiev',
            name='temperature_night',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='weatherkiev',
            name='date',
            field=models.CharField(default='', max_length=50),
        ),
    ]
