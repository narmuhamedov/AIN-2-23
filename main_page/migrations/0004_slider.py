# Generated by Django 4.2.7 on 2023-11-16 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_afishatable_alter_filmmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide', models.URLField()),
            ],
        ),
    ]
