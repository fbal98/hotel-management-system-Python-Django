# Generated by Django 3.0.8 on 2020-08-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0002_auto_20200821_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='customerName',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
