# Generated by Django 3.0.2 on 2020-02-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0002_auto_20200214_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='pdf',
            field=models.FileField(upload_to='upload'),
        ),
    ]