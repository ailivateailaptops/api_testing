# Generated by Django 5.1.6 on 2025-02-19 09:49

import django.core.validators
import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_url',
            field=models.URLField(blank=True, null=True, validators=[students.models.validate_custom_url]),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Age cannot be negative.'), django.core.validators.MaxValueValidator(120, message='Age cannot be more than 120.')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=2, validators=[students.models.validate_grade]),
        ),
    ]
