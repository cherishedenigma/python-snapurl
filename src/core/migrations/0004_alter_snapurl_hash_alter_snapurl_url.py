# Generated by Django 4.0.3 on 2022-03-17 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_post_origin_alter_snapurl_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snapurl',
            name='hash',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='snapurl',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
