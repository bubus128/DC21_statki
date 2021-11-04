# Generated by Django 3.2.5 on 2021-10-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20211030_1259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehregister',
            name='wielkosc_zanurzenia',
        ),
        migrations.AddField(
            model_name='vehregister',
            name='dowod_potwierdzajacy_wlasnosc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='vehregister',
            name='glebokosc_zanurzenia',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='dlugosc',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='dopuszczenie_pojazdu',
            field=models.CharField(blank=True, choices=[('Pojazd ma dopuszczenie indywidualne europejskie WE', 'Pojazd ma dopuszczenie indywidualne europejskie WE'), ('Pojazd ma dopuszczenie jednostkowe', 'Pojazd ma dopuszczenie jednostkowe')], default='Pojazd ma dopuszczenie indywidualne europejskie WE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='rok_produkcji',
            field=models.DecimalField(blank=True, decimal_places=0, default=2021, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='szerokosc',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='waga',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000, null=True),
        ),
        migrations.AlterField(
            model_name='vehregister',
            name='wysokosc_nad_poziomem_wody',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10000, null=True),
        ),
    ]