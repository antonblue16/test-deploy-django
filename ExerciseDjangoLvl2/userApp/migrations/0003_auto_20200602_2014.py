# Generated by Django 3.0.3 on 2020-06-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0002_auto_20200602_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='firstName',
            field=models.CharField(max_length=200),
        ),
    ]
