# Generated by Django 5.0 on 2023-12-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mission', models.TextField()),
                ('startDate', models.DateField()),
                ('duration', models.IntegerField()),
                ('isCompleted', models.BooleanField(default=False)),
            ],
        ),
    ]