# Generated by Django 3.2.16 on 2023-01-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_merge_20230103_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updateViaEmail',
            field=models.BooleanField(default=True, verbose_name='Update via email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updateViaPhoneNumber',
            field=models.BooleanField(default=False, verbose_name='Update via phone number'),
        ),
    ]