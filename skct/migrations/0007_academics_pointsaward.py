# Generated by Django 3.0.2 on 2020-03-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0006_academics_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='academics',
            name='pointsaward',
            field=models.IntegerField(default='0'),
        ),
    ]
