# Generated by Django 4.2.7 on 2023-12-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_task_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='update',
            field=models.TextField(null=True),
        ),
    ]