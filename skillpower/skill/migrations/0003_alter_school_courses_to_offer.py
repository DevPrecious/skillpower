# Generated by Django 3.2.7 on 2021-09-09 14:33

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='courses_to_offer',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Web design and development', 'Web design and development'), ('Photography and editing', 'Photography and editing'), ('Cinematography', 'Cinematography'), ('Fashion design expert', 'Fashion design expert'), ('Digital marketing specialist', 'Digital marketing specialist'), ('Creative graphics design', 'Creative graphics design'), ('IT support and solution master', 'IT support and solution master'), ('Data analyst', 'Data analyst'), ('Cake and confectionaries', 'Cake and confectionaries'), ('Copy writing mastery', 'Copy writing mastery'), ('Complete cosmetology', 'Complete cosmetology'), ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'), ('Hair dressing and wig making', 'Hair dressing and wig making')], max_length=330),
        ),
    ]
