# Generated by Django 2.1.14 on 2020-01-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0002_auto_20200124_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typecomponent',
            name='type',
        ),
        migrations.AddField(
            model_name='typecomponent',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
