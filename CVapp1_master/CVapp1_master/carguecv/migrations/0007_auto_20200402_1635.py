# Generated by Django 3.0.4 on 2020-04-02 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carguecv', '0006_carga_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga_cv',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carguecv.Cargo'),
        ),
    ]
