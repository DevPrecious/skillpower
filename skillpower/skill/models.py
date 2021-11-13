from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from PIL import Image
from multiselectfield import MultiSelectField

# Create your models here.

class Profile(models.Model):
    CHOICES = (
        ('School', 'SCHOOL'),
        ('Office', 'OFFICE'),
        ('Community', 'COMMUNITY')
    )
    user = models.OneToOneField(User, on_delete=CASCADE)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    organization = models.CharField(max_length=120, choices=CHOICES)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

class School(models.Model):
    CHOICES = (
        ('Web design and development', 'Web design and development'),
        ('Photography and editing', 'Photography and editing'),
        ('Cinematography', 'Cinematography'),
        ('Fashion design expert', 'Fashion design expert'),
        ('Digital marketing specialist', 'Digital marketing specialist'),
        ('Creative graphics design', 'Creative graphics design'),
        ('IT support and solution master', 'IT support and solution master'),
        ('Data analyst', 'Data analyst'),
        ('Cake and confectionaries', 'Cake and confectionaries'),
        ('Copy writing mastery', 'Copy writing mastery'),
        ('Complete cosmetology', 'Complete cosmetology'),
        ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'),
        ('Hair dressing and wig making', 'Hair dressing and wig making'),
    )
    user = models.OneToOneField(User, on_delete=CASCADE)
    name_of_school = models.CharField(null=True, max_length=120)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    number_of_students = models.IntegerField(default=0, null=True)
    courses_to_offer = MultiSelectField(choices=CHOICES)
    additional_information = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name_of_school} Data'

class Office(models.Model):
    CHOICES = (
        ('Web design and development', 'Web design and development'),
        ('Photography and editing', 'Photography and editing'),
        ('Cinematography', 'Cinematography'),
        ('Fashion design expert', 'Fashion design expert'),
        ('Digital marketing specialist', 'Digital marketing specialist'),
        ('Creative graphics design', 'Creative graphics design'),
        ('IT support and solution master', 'IT support and solution master'),
        ('Data analyst', 'Data analyst'),
        ('Cake and confectionaries', 'Cake and confectionaries'),
        ('Copy writing mastery', 'Copy writing mastery'),
        ('Complete cosmetology', 'Complete cosmetology'),
        ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'),
        ('Hair dressing and wig making', 'Hair dressing and wig making'),
    )
    user = models.OneToOneField(User, on_delete=CASCADE)
    name_of_office = models.CharField(null=True, max_length=120)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    number_of_staffs = models.IntegerField(default=0, null=True)
    courses_to_offer = MultiSelectField(choices=CHOICES)
    additional_information = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name_of_office} Data'

class Community(models.Model):
    CHOICES = (
        ('Web design and development', 'Web design and development'),
        ('Photography and editing', 'Photography and editing'),
        ('Cinematography', 'Cinematography'),
        ('Fashion design expert', 'Fashion design expert'),
        ('Digital marketing specialist', 'Digital marketing specialist'),
        ('Creative graphics design', 'Creative graphics design'),
        ('IT support and solution master', 'IT support and solution master'),
        ('Data analyst', 'Data analyst'),
        ('Cake and confectionaries', 'Cake and confectionaries'),
        ('Copy writing mastery', 'Copy writing mastery'),
        ('Complete cosmetology', 'Complete cosmetology'),
        ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'),
        ('Hair dressing and wig making', 'Hair dressing and wig making'),
    )
    user = models.OneToOneField(User, on_delete=CASCADE)
    # name_of_office = models.CharField(null=True, max_length=120)
    address = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    # number_of_staffs = models.IntegerField(default=0, null=True)
    courses_to_offer = MultiSelectField(choices=CHOICES)
    additional_information = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user} Data'

class Student(models.Model):
    CHOICES = (
        ('Web design and development', 'Web design and development'),
        ('Photography and editing', 'Photography and editing'),
        ('Cinematography', 'Cinematography'),
        ('Fashion design expert', 'Fashion design expert'),
        ('Digital marketing specialist', 'Digital marketing specialist'),
        ('Creative graphics design', 'Creative graphics design'),
        ('IT support and solution master', 'IT support and solution master'),
        ('Data analyst', 'Data analyst'),
        ('Cake and confectionaries', 'Cake and confectionaries'),
        ('Copy writing mastery', 'Copy writing mastery'),
        ('Complete cosmetology', 'Complete cosmetology'),
        ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'),
        ('Hair dressing and wig making', 'Hair dressing and wig making'),
    )
    school = models.ForeignKey(User, on_delete=CASCADE, default=None)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    student_class = models.CharField(max_length=225)
    age = models.IntegerField(default=0)
    course_to_take = MultiSelectField(choices=CHOICES)

    def __str__(self):
        return f'{self.school.username} added {self.first_name}'

class Staff(models.Model):
    CHOICES = (
        ('Web design and development', 'Web design and development'),
        ('Photography and editing', 'Photography and editing'),
        ('Cinematography', 'Cinematography'),
        ('Fashion design expert', 'Fashion design expert'),
        ('Digital marketing specialist', 'Digital marketing specialist'),
        ('Creative graphics design', 'Creative graphics design'),
        ('IT support and solution master', 'IT support and solution master'),
        ('Data analyst', 'Data analyst'),
        ('Cake and confectionaries', 'Cake and confectionaries'),
        ('Copy writing mastery', 'Copy writing mastery'),
        ('Complete cosmetology', 'Complete cosmetology'),
        ('Professional animation maker and motion graphics', 'Professional animation maker and motion graphics'),
        ('Hair dressing and wig making', 'Hair dressing and wig making'),
    )
    office = models.ForeignKey(User, on_delete=CASCADE, default=None)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    department = models.CharField(max_length=225)
    age = models.IntegerField(default=0)
    course_to_take = MultiSelectField(choices=CHOICES)

    def __str__(self):
        return f'{self.office.username} added {self.first_name}'


