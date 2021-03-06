# Generated by Django 2.2.5 on 2022-01-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0003_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class_Board',
            fields=[
                ('cb_id', models.AutoField(primary_key=True, serialize=False)),
                ('cb_date', models.DateTimeField()),
                ('subject', models.CharField(max_length=150, null=True)),
                ('today_class', models.CharField(max_length=150, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'Class_Board',
                'managed': False,
            },
        ),
    ]
