# Generated by Django 2.2.6 on 2019-10-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogmain', '0003_auto_20191027_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_picture',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]