# Generated by Django 4.2.3 on 2023-07-29 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_remove_habit_has_auxiliary_habits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auxiliaryhabit',
            name='main_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auxiliary_habit', to='habits.habit', verbose_name='main_habit'),
        ),
    ]
