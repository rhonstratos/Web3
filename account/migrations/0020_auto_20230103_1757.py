# Generated by Django 3.2.16 on 2023-01-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_merge_20230103_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='notifyMode',
            field=models.CharField(blank=True, choices=[('email', 'Via Email'), ('phone_number', 'Via Phone Number'), ('both', 'Both Via Email and Phone Number')], max_length=12, null=True, verbose_name='Update User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(default='-', max_length=20, verbose_name='Phone Number'),
        ),
    ]