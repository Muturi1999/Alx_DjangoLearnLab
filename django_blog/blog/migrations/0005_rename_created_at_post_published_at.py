# Generated by Django 5.1.7 on 2025-03-21 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='published_at',
        ),
    ]
