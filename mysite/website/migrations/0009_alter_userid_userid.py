# Generated by Django 3.2.9 on 2022-01-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_alter_userid_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userid',
            name='userId',
            field=models.CharField(default=74589061, max_length=1000000),
        ),
    ]