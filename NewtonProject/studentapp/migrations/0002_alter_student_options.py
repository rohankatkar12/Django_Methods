# Generated by Django 4.2.2 on 2023-08-09 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['student_name'], 'verbose_name': 'Student'},
        ),
    ]