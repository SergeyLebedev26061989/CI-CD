# Generated by Django 4.1.5 on 2023-02-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.BigAutoField(auto_created=True,
                                      primary_key=True,
                                      serialize=False,
                                      verbose_name='ID'),
        ),
    ]
