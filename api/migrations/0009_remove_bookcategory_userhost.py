# Generated by Django 3.2.8 on 2021-10-10 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_bookcategory_userhost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcategory',
            name='userhost',
        ),
    ]
