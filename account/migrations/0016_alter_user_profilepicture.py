# Generated by Django 3.2.16 on 2023-01-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_user_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilePicture',
            field=models.ImageField(blank=True, default='profileImages/no-profile-picture-icon.webp', null=True, upload_to='profileImages', verbose_name='Profile Picture'),
        ),
    ]
