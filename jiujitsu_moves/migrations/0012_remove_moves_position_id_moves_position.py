# Generated by Django 4.1 on 2022-12-08 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jiujitsu_moves', '0011_testfk_calltestfk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moves',
            name='position_id',
        ),
        migrations.AddField(
            model_name='moves',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jiujitsu_moves.positions'),
        ),
    ]