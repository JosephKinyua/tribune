# Generated by Django 3.1.3 on 2021-09-02 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210901_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='articles/'),
            preserve_default=False,
        ),
    ]
