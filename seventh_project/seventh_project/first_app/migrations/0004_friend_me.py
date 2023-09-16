# Generated by Django 4.2.5 on 2023-09-16 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_employeemodel_managermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=10)),
                ('attendence', models.BooleanField()),
                ('hw', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Me',
            fields=[
                ('friend_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.friend')),
            ],
            bases=('first_app.friend',),
        ),
    ]
