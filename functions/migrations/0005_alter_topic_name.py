# Generated by Django 4.0.6 on 2022-07-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('functions', '0004_rename_problems_problem_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
