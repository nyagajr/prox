# Generated by Django 3.0 on 2021-03-14 19:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_article_article_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='content_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
