# Generated by Django 3.1.3 on 2021-09-01 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]