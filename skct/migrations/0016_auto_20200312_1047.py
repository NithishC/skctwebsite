# Generated by Django 3.0.2 on 2020-03-12 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0015_auto_20200310_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
