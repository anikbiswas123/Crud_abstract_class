# Generated by Django 4.1.7 on 2023-03-28 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distr', models.CharField(max_length=400)),
                ('sub_distr', models.CharField(max_length=300)),
                ('address', models.TextField(max_length=400)),
                ('cust_name', models.CharField(max_length=50)),
                ('cust_email', models.CharField(max_length=20)),
                ('cust_Phon', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='emplopyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distr', models.CharField(max_length=400)),
                ('sub_distr', models.CharField(max_length=300)),
                ('address', models.TextField(max_length=400)),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_post', models.CharField(max_length=20)),
                ('emp_salary', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
