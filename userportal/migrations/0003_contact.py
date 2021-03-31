# Generated by Django 3.0.8 on 2021-03-26 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userportal', '0002_auto_20210325_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_first_name', models.CharField(max_length=30)),
                ('c_last_name', models.CharField(max_length=30)),
                ('c_email', models.EmailField(max_length=200)),
                ('c_msg', models.CharField(max_length=255)),
            ],
        ),
    ]
