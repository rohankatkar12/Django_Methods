# Generated by Django 4.2.2 on 2023-08-04 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegeapp', '0002_rename_reciepe_description_receipe_receipe_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='reciepeimage'),
        ),
    ]
