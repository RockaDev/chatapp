# Generated by Django 3.2.9 on 2022-01-21 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_userid_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userid',
            name='id',
        ),
        migrations.AlterField(
            model_name='userid',
            name='userId',
            field=models.CharField(default=92711016, max_length=1000000, primary_key=True, serialize=False),
        ),
    ]
