# Generated by Django 3.2.9 on 2022-01-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20220121_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userid',
            name='userId',
            field=models.CharField(default=3569125, max_length=1000000),
        ),
    ]
