# Generated by Django 4.2.11 on 2024-04-10 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs_app', '0003_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_author',
        ),
    ]
