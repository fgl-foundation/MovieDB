# Generated by Django 2.2.4 on 2019-11-11 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('List', '0005_auto_20191112_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeed',
            name='lastaction',
            field=models.TextField(blank=True),
        ),
    ]