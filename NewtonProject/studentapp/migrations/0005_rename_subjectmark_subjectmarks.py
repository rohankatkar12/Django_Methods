# Generated by Django 4.2.2 on 2023-08-12 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_rename_subjectmarks_subjectmark'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubjectMark',
            new_name='SubjectMarks',
        ),
    ]
