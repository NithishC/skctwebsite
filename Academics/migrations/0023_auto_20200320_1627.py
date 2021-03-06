# Generated by Django 3.0.2 on 2020-03-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0022_auto_20200320_1301'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectGuidance',
        ),
        migrations.AddField(
            model_name='allclear',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='awards',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='extracurricular',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='internship',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='onlinecertification',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='pg',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='prizes',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='startups',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='studentactivities',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='threeclear',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
        migrations.AddField(
            model_name='ug',
            name='dept',
            field=models.CharField(default='Null', max_length=5),
        ),
    ]
