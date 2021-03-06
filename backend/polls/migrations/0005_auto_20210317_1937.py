# Generated by Django 2.2 on 2021-03-17 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210317_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='datetime uploaded'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='datetime uploaded'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='story',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='datetime uploaded'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='datetime uploaded'),
            preserve_default=False,
        ),
    ]
