# Generated by Django 4.2.13 on 2024-05-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comment', models.TextField(verbose_name='하고 싶은 말')),
                ('answers', models.CharField(max_length=25)),
            ],
        ),
    ]
