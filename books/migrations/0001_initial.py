# Generated by Django 2.1.3 on 2018-11-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
