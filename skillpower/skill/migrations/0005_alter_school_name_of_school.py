# Generated by Django 3.2.7 on 2021-09-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0004_school_name_of_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name_of_school',
            field=models.CharField(default=0, max_length=120),
        ),
    ]