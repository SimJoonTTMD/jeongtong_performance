# Generated by Django 3.1.2 on 2020-12-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_guestbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestbook',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
