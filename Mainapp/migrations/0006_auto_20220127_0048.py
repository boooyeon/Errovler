# Generated by Django 2.2.5 on 2022-01-27 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_total_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_Comment',
            fields=[
                ('c_no', models.AutoField(primary_key=True, serialize=False)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
                ('contents', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'Total_Comment',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
