# Generated by Django 3.0.5 on 2020-04-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0006_auto_20200411_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='disctiption',
            field=models.TextField(blank=True, null=True),
        ),
    ]