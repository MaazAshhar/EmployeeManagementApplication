# Generated by Django 4.2.4 on 2023-08-22 16:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('testimonial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
    ]