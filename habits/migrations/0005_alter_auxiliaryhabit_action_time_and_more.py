# Generated by Django 4.2.3 on 2023-07-29 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliaryhabit',
            name='action_time',
            field=models.TimeField(blank=True, null=True, verbose_name='auxiliary_action_time'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='action_time',
            field=models.TimeField(verbose_name='action_time'),
        ),
    ]
