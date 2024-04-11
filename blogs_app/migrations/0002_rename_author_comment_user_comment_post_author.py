# Generated by Django 4.2.11 on 2024-04-10 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='blogs_app.post'),
            preserve_default=False,
        ),
    ]