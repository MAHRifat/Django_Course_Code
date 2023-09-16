# Generated by Django 4.2.5 on 2023-09-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_remove_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('roll', models.IntegerField()),
                ('class_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('subject', models.CharField(max_length=20)),
                ('mobile_num', models.CharField(max_length=11)),
                ('student', models.ManyToManyField(to='first_app.student')),
            ],
        ),
    ]
