# Generated by Django 3.2.7 on 2021-09-10 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skill', '0008_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('courses_to_offer', multiselectfield.db.fields.MultiSelectField(choices=[('Web design and development', 'Web design and development'), ('Photography and editing', 'Photography and editing'), ('Cinematography', 'Cinematography'), ('Fashion design expert', 'Fashion design expert'), ('Digital marketing specialist', 'Digital marketing specialist'), ('Creative graphics design', 'Creative graphics design'), ('IT support and solution master', 'IT support and solution master'), ('Data analyst', 'Data analyst'), ('Cake and confectionaries', 'Cake and confectionaries'), ('Copy writing mastery', 'Copy writing mastery'), ('Complete cosmetology', 'Complete cosmetology'), ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'), ('Hair dressing and wig making', 'Hair dressing and wig making')], max_length=330)),
                ('additional_information', models.TextField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
