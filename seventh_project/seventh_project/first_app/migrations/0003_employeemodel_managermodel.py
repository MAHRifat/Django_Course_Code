# Generated by Django 4.2.5 on 2023-09-16 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_studentinfomodel_teacherinfomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerModel',
            fields=[
                ('employeemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employeemodel')),
                ('take_interview', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
            bases=('first_app.employeemodel',),
        ),
    ]