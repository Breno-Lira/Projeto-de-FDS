# Generated by Django 4.2.8 on 2024-04-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Real',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('participants', models.CharField(max_length=200)),
            ],
        ),
    ]
