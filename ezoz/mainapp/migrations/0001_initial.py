# Generated by Django 3.2.9 on 2022-01-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('number', models.CharField(max_length=16)),
                ('info', models.TextField()),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('video', models.FileField(null=True, upload_to='')),
                ('price', models.CharField(max_length=16)),
            ],
        ),
    ]
