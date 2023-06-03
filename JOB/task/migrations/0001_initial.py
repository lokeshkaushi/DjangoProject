# Generated by Django 4.1.2 on 2022-10-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='', max_length=100)),
                ('blog_name', models.CharField(default='', max_length=200)),
                ('created_date', models.DateTimeField(default='')),
                ('update_date', models.DateTimeField(default='')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Calendar', models.DateTimeField()),
                ('food', models.CharField(max_length=50)),
                ('Travel', models.CharField(max_length=50)),
                ('Fashion', models.CharField(max_length=50)),
                ('Technology', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
