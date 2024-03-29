# Generated by Django 2.0.2 on 2018-04-01 09:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.TextField()),
                ('MobilePhone', models.TextField()),
                ('Group', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.TextField()),
                ('StudentNumber', models.IntegerField()),
                ('Detail', models.TextField()),
                ('Requirements', models.TextField()),
                ('TagofProject', models.TextField()),
                ('status', models.IntegerField()),
                ('Professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KarshenasiDjango.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('FullName', models.TextField()),
                ('MobilePhone', models.TextField()),
                ('StudentField', models.IntegerField()),
                ('StudentUnits', models.IntegerField(null=True)),
                ('StudentNumber', models.IntegerField(null=True)),
                ('StudentPrf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KarshenasiDjango.Professor')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KarshenasiDjango.Professor')),
                ('Student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KarshenasiDjango.Student')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
