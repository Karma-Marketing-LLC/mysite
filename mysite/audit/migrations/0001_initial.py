# Generated by Django 2.2.6 on 2019-10-29 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_title', models.CharField(max_length=35, verbose_name='Lead Name')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50, verbose_name='Contact Name')),
                ('met_d_time', models.DateTimeField(verbose_name='Meeting Date & Time')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Lead')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=50, verbose_name='Organization Name')),
                ('month_rec_rev', models.PositiveIntegerField(verbose_name='Monthly Recurring Revenue')),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.Lead')),
            ],
        ),
    ]
