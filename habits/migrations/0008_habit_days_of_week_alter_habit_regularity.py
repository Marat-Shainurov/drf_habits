# Generated by Django 4.2.3 on 2023-08-01 10:41

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_habit_regularity'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='days_of_week',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('mon', 'Every Monday'), ('tue', 'Every Tuesday'), ('wed', 'Every Wednesday'), ('thu', 'Every Thursday'), ('fri', 'Every Friday'), ('sat', 'Every Saturday'), ('sun', 'Every Sunday')], max_length=3, null=True, verbose_name='days_of_week'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='regularity',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly')], default='daily', max_length=7, verbose_name='habit_regularity'),
        ),
    ]
