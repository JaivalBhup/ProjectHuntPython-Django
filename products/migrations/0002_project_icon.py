# Generated by Django 3.0.1 on 2020-01-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='icon',
            field=models.ImageField(default='static/monitor.png', upload_to='images/'),
        ),
    ]
