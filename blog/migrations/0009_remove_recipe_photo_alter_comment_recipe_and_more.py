# Generated by Django 4.2.10 on 2024-03-03 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_recipe_likes_alter_comment_recipe_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='photo',
        ),
        migrations.AlterField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comments', to='blog.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='recipe_comments', to='blog.comment'),
        ),
    ]
