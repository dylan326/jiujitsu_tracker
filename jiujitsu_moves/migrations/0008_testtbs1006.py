# Generated by Django 4.1 on 2022-10-07 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiujitsu_moves', '0007_delete_testtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='testtbs1006',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testfield', models.CharField(max_length=64)),
            ],
        ),
    ]
