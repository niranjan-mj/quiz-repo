# Generated by Django 2.0 on 2019-08-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20190830_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]