# Generated by Django 3.2.7 on 2021-09-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0003_alter_school_courses_to_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='name_of_school',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
