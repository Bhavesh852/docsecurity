# Generated by Django 3.0.8 on 2021-03-25 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Private_Doc',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('pdoc_category', models.CharField(max_length=20)),
                ('pdoc_title', models.CharField(max_length=30)),
                ('pdoc_tech', models.CharField(max_length=30)),
                ('pdoc_pass', models.CharField(max_length=20)),
                ('pdoc', models.FileField(upload_to='userportal/document')),
                ('pdoc_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doc_Detail',
            fields=[
                ('doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('doc_category', models.CharField(max_length=20)),
                ('doc_title', models.CharField(max_length=30)),
                ('doc_tech', models.CharField(max_length=30)),
                ('doc', models.FileField(upload_to='userportal/document')),
                ('doc_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
