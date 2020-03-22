# Generated by Django 3.0.2 on 2020-02-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload/%User/%Y/%m/%d/')),
            ],
        ),
    ]