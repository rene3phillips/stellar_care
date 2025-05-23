# Generated by Django 5.2.1 on 2025-05-23 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0009_alter_billing_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='date_hired',
            field=models.DateField(default=datetime.date(1990, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='license_number',
            field=models.CharField(default='0123', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default='123-1234', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='billing',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2025, 6, 22, 18, 37, 23, 131184, tzinfo=datetime.timezone.utc)),
        ),
    ]
