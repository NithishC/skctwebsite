# Generated by Django 3.0.2 on 2020-03-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0013_auto_20200310_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proof',
            name='des',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
