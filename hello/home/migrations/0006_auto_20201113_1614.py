# Generated by Django 3.1.3 on 2020-11-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='link',
            field=models.FileField(upload_to='pdf'),
        ),
    ]
