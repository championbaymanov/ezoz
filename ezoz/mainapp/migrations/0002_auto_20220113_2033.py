# Generated by Django 3.2.9 on 2022-01-13 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thik_font', models.TextField()),
                ('thin_font', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FirstSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SecondComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thik_font', models.TextField()),
                ('thin_font', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
