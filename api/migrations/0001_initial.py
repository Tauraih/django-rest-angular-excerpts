# Generated by Django 3.0.8 on 2020-07-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('year', models.DateTimeField()),
            ],
        ),
    ]
