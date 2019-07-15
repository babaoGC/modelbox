# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-14 12:10
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('face', models.FileField(default='face/default.png', upload_to='face/')),
                ('user_type', models.IntegerField(choices=[(1, '管理员'), (0, '普通用户')], default=0)),
                ('points', models.IntegerField(default=0, null=True)),
                ('is_locked', models.IntegerField(default=0, null=True)),
                ('purse', models.IntegerField(default=0, null=True)),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.IntegerField()),
                ('collect_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=255)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('parent', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_user', models.IntegerField()),
                ('f_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('path', models.CharField(max_length=255)),
                ('md5', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('file_size', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=9, null=True)),
                ('collect_num', models.IntegerField(default=0, null=True)),
                ('download_num', models.IntegerField(default=0, null=True)),
                ('version', models.IntegerField(choices=[(0, 'SketchUp 8.0'), (1, 'SketchUp 2013'), (2, 'SketchUp 2014'), (3, 'SketchUp 2015'), (4, 'SketchUp 2016'), (5, 'SketchUp 2017'), (6, 'SketchUp 2018'), (7, 'SketchUp 2019')], default=0)),
                ('style', models.IntegerField(choices=[(0, '现代'), (1, '中式'), (2, '美式'), (3, '北欧')], default=0)),
                ('introduce', models.TextField(max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=5)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to='picture/')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Model')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='model',
            name='tag',
            field=models.ManyToManyField(to='app01.Tag'),
        ),
        migrations.AddField(
            model_name='model',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='download',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Model'),
        ),
        migrations.AddField(
            model_name='comment',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Model'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='collect',
            field=models.ManyToManyField(to='app01.Collect'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='download',
            field=models.ManyToManyField(to='app01.Download'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='follow',
            field=models.ManyToManyField(to='app01.Follow'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
