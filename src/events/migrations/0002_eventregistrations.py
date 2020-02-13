# Generated by Django 3.0.2 on 2020-02-13 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRegistrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('datetime_event', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=200)),
                ('price', models.FloatField(max_length=15)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('eaddress', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=15)),
                ('num_of_people', models.CharField(max_length=15)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField()),
                ('registration_status', models.CharField(choices=[('submitted', 'submitted'), ('confirmed', 'confirmed'), ('cancelled', 'cancelled')], default='submitted', max_length=20)),
            ],
        ),
    ]