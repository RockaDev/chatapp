# Generated by Django 3.2.9 on 2022-01-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_alter_userid_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='userid',
            name='rooms',
            field=models.CharField(default='', max_length=1000000),
        ),
    ]
