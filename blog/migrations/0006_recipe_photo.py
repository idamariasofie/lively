# Generated by Django 4.2.10 on 2024-02-29 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile_bio_profile_display_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='recipe_photos/'),
        ),
    ]
