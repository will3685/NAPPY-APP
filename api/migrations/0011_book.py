# Generated by Django 3.2.8 on 2021-10-10 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_userhost_bookcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.bookcategory')),
                ('userhost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='api.userhost')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]
