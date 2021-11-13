# Generated by Django 3.2.9 on 2021-11-11 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petitioner_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitioner_app.vehregister')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=60)),
                ('path', models.CharField(max_length=200)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petitioner_app.application')),
            ],
        ),
    ]
