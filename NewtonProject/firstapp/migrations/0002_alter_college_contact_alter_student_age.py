# Generated by Django 4.2.2 on 2023-06-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.SmallIntegerField(),
        ),
    ]
