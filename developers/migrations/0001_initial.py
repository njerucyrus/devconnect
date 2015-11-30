# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
import phonenumber_field.modelfields
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('idnumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('website', models.URLField()),
                ('organization', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=50)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('category', models.CharField(default=b'Java', max_length=50, choices=[(b'Java', b'Java'), (b'Python', b'Python'), (b'C#', b'C#'), (b'Ruby', b'Ruby'), (b'JavaScript', b'JavaScript')])),
                ('availability', models.CharField(default=b'Part Time', max_length=50, choices=[(b'Part Time', b'Part Time'), (b'Full Time', b'Full Time')])),
                ('education', models.TextField()),
                ('employment', models.TextField()),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('projects', models.TextField()),
                ('skills', models.TextField()),
                ('portfolio', models.TextField()),
                ('slug', models.SlugField(max_length=200, unique=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Developers List',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('idnumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('website', models.URLField()),
                ('organization', models.TextField()),
                ('description', models.TextField()),
                ('date_requested', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Employers List',
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('category', models.CharField(default=b'Hardware', max_length=50, choices=[(b'Hardware', b'Hardware'), (b'Software', b'Software'), (b'Support', b'Support'), (b'Design', b'Design')])),
            ],
            options={
                'managed': True,
                'verbose_name_plural': 'Jobs List',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'Developer', max_length=20, choices=[(b'Developer', b'Developer'), (b'Employer', b'Employer')])),
                ('activation_key', models.CharField(max_length=40, blank=True)),
                ('key_expires', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User profiles',
            },
        ),
        migrations.AddField(
            model_name='jobs',
            name='tags',
            field=models.ManyToManyField(to='developers.Tag'),
        ),
    ]
