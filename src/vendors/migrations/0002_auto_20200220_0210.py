# Generated by Django 3.0.2 on 2020-02-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='web_site',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
