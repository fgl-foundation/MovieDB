# Generated by Django 3.0.3 on 2020-03-16 05:17

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0004_auto_20200313_0407'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='movie',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='watchlist',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyWatchList.Season'),
        ),
    ]
