# Generated by Django 5.0.7 on 2024-08-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('bank', models.CharField(choices=[('AIB', 'Allied Irish Banks'), ('BOI', 'Bank of Ireland'), ('PTSB', 'Permanent TSB'), ('ANP', 'An Post Money'), ('REV', 'Revolut'), ('N26', 'N26'), ('CU', 'Credit Union'), ('OTH', 'Other')], max_length=4)),
                ('account_type', models.CharField(choices=[('PA', 'Personal Account'), ('BE', 'Business Entity')], max_length=2)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('logo', models.ImageField(upload_to='logos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('budget', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('is_essential', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
