from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),
)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name="username", blank=False, error_messages={'unique': "A user with that username already exists.",})
    email = models.EmailField(unique=True, blank=False, error_messages={'unique': "A user with that email already exists.",})
    phoneNumber = models.CharField(max_length=20, default='-', verbose_name='phone number', blank=False)
    role = models.CharField(choices=ROLE, max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)
    skills = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    experiences = models.TextField(blank=True, null=True)
    profilePicture = models.ImageField(blank=True, null=True, verbose_name='Profile Picture', upload_to='profileImages', default='profileImages/no-profile-picture-icon.webp')
    resume = models.FileField(upload_to='resumes', blank=True, null=True, verbose_name='Resume')
    category = models.ForeignKey('jobapp.Category',related_name='Category_user', on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()
