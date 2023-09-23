# Generated by Django 4.2.5 on 2023-09-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TO_Do_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasktitle', models.CharField(max_length=30)),
                ('taskDescription', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
