# Generated by Django 5.0.3 on 2024-04-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
