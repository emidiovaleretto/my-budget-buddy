# Generated by Django 5.0.7 on 2024-08-17 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='logos/'),
        ),
    ]