# Generated by Django 3.2.8 on 2021-10-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardPanel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github_username', models.CharField(max_length=127)),
                ('repo_name', models.CharField(max_length=127)),
                ('panel_type', models.CharField(choices=[('piechart', 'Pie-chart of languages used'), ('barchart', 'Bar-chart of languages used')], max_length=127)),
            ],
        ),
    ]