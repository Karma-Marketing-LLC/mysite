# Generated by Django 2.2.6 on 2019-11-05 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(default='home.models', max_length=255)),
                ('bg_label', models.CharField(default='/bg.jpg', max_length=255)),
                ('css_label', models.CharField(default='/theme.css', max_length=255)),
            ],
        ),
    ]
