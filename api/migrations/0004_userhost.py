# Generated by Django 3.2.8 on 2021-10-10 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_hair_observation'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=20)),
                ('host_email', models.EmailField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User_Host',
            },
        ),
    ]
