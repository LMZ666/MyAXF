# Generated by Django 2.1.2 on 2018-11-02 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='specifics',
            field=models.CharField(max_length=30),
        ),
    ]
