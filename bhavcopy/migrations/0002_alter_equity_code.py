# Generated by Django 3.2.12 on 2023-08-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bhavcopy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]