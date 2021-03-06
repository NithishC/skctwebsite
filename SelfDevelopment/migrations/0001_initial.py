# Generated by Django 3.0.2 on 2020-03-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Awards')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='ThreeClear')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='EventsParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Startups')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Excellence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Competitive')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Academics')),
                ('points', models.IntegerField(default=0)),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='GuestLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Feedback')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='GuestLectureIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Innovations')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MOU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Article')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineCertification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='UG')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='OnlineCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Prizes')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PatentFiled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='PG')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PatentGranted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='StudentActivities')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PatentPublished',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Extracurricular')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementArranged',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(default='Null', max_length=5)),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='Allclear')),
                ('points', models.IntegerField(default='0')),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
    ]
