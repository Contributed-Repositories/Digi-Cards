# Generated by Django 3.1.4 on 2020-12-04 12:38

import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0002_auto_20201130_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='desc',
            field=models.CharField(default='Description for the unit goes here!', max_length=100),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='background_img/card/'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='background_img/subject/'),
        ),
        migrations.AlterField(
            model_name='subunit',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='background_img/subunit/'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='background_img/unit/'),
        ),
    ]