# Generated by Django 4.1 on 2022-09-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=100)),
                ('dob', models.CharField(default='', max_length=100)),
                ('mobile', models.BigIntegerField(default=10)),
            ],
        ),
    ]