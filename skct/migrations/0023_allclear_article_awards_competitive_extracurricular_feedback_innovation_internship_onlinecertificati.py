# Generated by Django 3.0.2 on 2020-03-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0022_auto_20200315_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllClear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Competitive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraCurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Innovation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Prizes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGuidance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Startups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='StudentActivities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ThreeClear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
    ]
