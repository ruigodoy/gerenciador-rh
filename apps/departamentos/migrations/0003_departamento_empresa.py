# Generated by Django 3.1.4 on 2020-12-25 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('departamentos', '0002_auto_20201218_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
    ]
