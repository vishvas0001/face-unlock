# Generated by Django 2.0.9 on 2018-11-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unlocker', '0004_onetimerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimerequest',
            name='image',
            field=models.FileField(upload_to='images/onetime/'),
        ),
    ]
