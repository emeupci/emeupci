# Generated by Django 2.1.5 on 2019-02-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='City name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='', max_length=255, verbose_name='Country name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=255, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=255, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=255, verbose_name='First name'),
            preserve_default=False,
        ),
    ]
