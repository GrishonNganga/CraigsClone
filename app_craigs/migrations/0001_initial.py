# Generated by Django 2.2.7 on 2019-11-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_field', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
