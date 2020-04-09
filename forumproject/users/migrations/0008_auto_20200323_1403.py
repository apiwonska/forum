# Generated by Django 3.0.3 on 2020-03-23 14:03

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200320_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='users/blank-profile-picture.svg', upload_to='users/'),
        ),
    ]