# Generated by Django 4.2.3 on 2023-07-29 12:15

from django.db import migrations, models
import users.services


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=users.services.upload_path, verbose_name='user_avatar'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='telegram',
            field=models.CharField(default='@mshaynurov', max_length=50, unique=True, verbose_name='user_phone'),
            preserve_default=False,
        ),
    ]