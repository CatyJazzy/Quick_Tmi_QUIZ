# Generated by Django 4.2.13 on 2024-05-13 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_user_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='answers',
            field=models.IntegerField(),
        ),
    ]