# Generated by Django 3.0.2 on 2020-02-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('time_to_read_min', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
