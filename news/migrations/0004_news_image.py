# Generated by Django 4.0.6 on 2022-07-30 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=0, upload_to='news/images/'),
            preserve_default=False,
        ),
    ]
