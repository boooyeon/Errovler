# Generated by Django 2.2.5 on 2022-01-24 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Member',
                'managed': False,
            },
        ),
    ]
