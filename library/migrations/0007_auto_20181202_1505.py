# Generated by Django 2.1.3 on 2018-12-02 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20181202_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amanat',
            name='id',
        ),
        migrations.AlterField(
            model_name='amanat',
            name='id_book_amanat',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
